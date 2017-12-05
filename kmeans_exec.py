import math, sys
from operator import add
from pyspark import SparkContext

# Usage: kmeans_exec.py <input file> <k> <distance measure>
# spark-submit --master yarn-cluster kmeans_exec.py lat_longs_test.txt 4
# spark-submit --master yarn-client kmeans_exec.py lat_longs_test.txt 4
# spark-submit --master local[*] kmeans_exec.py lat_longs_test.txt 4
if __name__ == "__main__":
    sc = SparkContext()

    input_file = sys.argv[1]
    k = int(sys.argv[2])
    distance_measure = 'Euclidean'
    print("Reading from %s, k value %s" % (input_file, k))

    def addPoints(p1,p2):
        return map(add, p1, p2)

    def EuclideanDistance(p1, p2):
        return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def closestPoint(p, centers):
        distances = [EuclideanDistance(p, center) for center in centers]
        return distances.index(min(distances))

    def GreatCircleDistance(p1, p2):
        pass

    # read data and parse
    dat = sc.textFile(input_file).map(lambda line: line.split(' '))

    # augment the points by 1 to keep track of number of points summed
    points = dat.map(lambda p: (float(p[0]), float(p[1]), 1))
    points.persist()

    # random generate initial k centers
    centers = [(point[0], point[1]) for point in points.takeSample(True, k)]
    print("Initial centers:")
    print(centers)
    new_centers = [(0,0)] * k
    error = 0
    errors = []
    convergeDist = 0.1
    change = 1
    iteration = 1

    print("Starting training..")
    # iterate until converge
    while change > convergeDist:
        print("Iteration: %s" % iteration)
        # produce (center index, augmented point) pair
        center_point = points.keyBy(lambda point: closestPoint(point[:2], centers))
        # compute the error
        error = center_point.map(lambda (ci, p): EuclideanDistance(centers[ci], p)**2).reduce(lambda v1, v2: v1+v2)
        errors.append(error)
        print("Error of current center: %s" % error)
        # sum all point coordinate for each cluster
        sums = center_point.reduceByKey(addPoints).collect()
        # get new center by taking avg of coordinate sums
        new_centers = [c[1:] for c in sorted([(s[0], float(s[1][0])/s[1][2], float(s[1][1])/s[1][2]) for s in sums], key = lambda center: center[0])]
        print("New centers: ")
        print(new_centers)
        # see if change of centers are small enough for termination
        change = sum([EuclideanDistance(old, new) for (old, new) in zip(centers, new_centers)])
        print("Change since last center: %s" % change)
        # update the centers
        centers = list(new_centers)
        iteration += 1

    # output final centers
    centers_final = centers
    print("Final centers: ")
    print(centers_final)
    print("Errors: ")
    print(errors)

    sc.parallelize(centers_final).saveAsTextFile('final_centers')

    # final clusters
    final_clusters = points.keyBy(lambda point: closestPoint(point[:2], centers_final))

    def RDD_to_lines(dat):
        return ','.join([str(dat[0]), str(dat[1][0]), str(dat[1][1])])

    lines = final_clusters.map(RDD_to_lines)
    lines.saveAsTextFile('final_clusters')
