import math
from operator import add

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
dat = sc.textFile("lat_longs_test.txt").map(lambda line: line.split(' '))

# augment the points by 1 to keep track of number of points summed
points = dat.map(lambda p: (float(p[0]), float(p[1]), 1))
# initialize vars
initial_centers = [(-90,-90), (90,90), (-90,90), (90, -90)]
centers = initial_centers
error = 0
errors = []
min_change = 0.01
change = 1
# iterate until converge
while change > min_change:
    # produce (center index, augmented point) pair
    center_point = points.keyBy(lambda point: closestPoint(point[:2], centers))
    # sum all point coordinate for each cluster
    sums = center_point.reduceByKey(addPoints)
    # compute the error
    error = center_point.map(lambda (ci, p): EuclideanDistance(centers[ci], p)**2).reduce(lambda v1, v2: v1+v2)
    errors.append(error)
    # get new center by taking avg of coordinate sums
    new_centers = sums.map(lambda (i, cen): (float(cen[0])/cen[2], float(cen[1])/cen[2])).collect()
    # see if change of centers are small enough for termination
    change = sum([EuclideanDistance(old, new) for (old, new) in zip(centers, new_centers)])
    # update the centers
    centers = new_centers

# output final centers
centers_final = centers
print("Final centers: ")
print(centers_final)

# visualization
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

initial_centers = [(-90,-90), (90,90), (-90,90), (90, -90)]
final_centers = [(-3.3317347701149425, -62.14183170498081),
 (43.22474153743314, 10.419616617548034),
 (19.62659117762128, 104.22780737480441),
 (37.821261279683874, -96.58667536271501)]

# read in sample data and parse
with open('lat_longs_sample.txt', 'r') as f:
    points = [(float(points[0]), float(points[1])) for points in [line.split(' ') for line in f.readlines()]]

# voronoi plot using final center
vor = Voronoi(final_centers)
voronoi_plot_2d(vor)

# scatter points and centers
plt.scatter([p[0] for p in points], [p[1] for p in points], marker='.')
plt.scatter([c[0] for c in final_centers], [c[1] for c in final_centers], marker='o', s=80, facecolors='r', edgecolors='r')
plt.scatter([c[0] for c in initial_centers], [c[1] for c in initial_centers], marker='o', s=80, facecolors='b', edgecolors='b')
axes = plt.gca()
axes.set_xlim([-180, 180])
axes.set_ylim([-180, 180])
plt.show()
