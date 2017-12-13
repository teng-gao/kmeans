#Citation for formula used: https://superuser.com/questions/602798/how-to-do-a-great-circle-calculation-in-ms-excel-or-libreoffice
import math, sys
from operator import add

# Usage: python calc_final_errors.py <clusters file> <centers file> <distance measure> <out_file>
# python ../../scripts/calc_final_errs.py clusters.txt centers.txt Euclidean final_error.txt

cluster_file = str(sys.argv[1])
centers_file = str(sys.argv[2])
distance_measure = str(sys.argv[3])
out_file = str(sys.argv[4])

def EuclideanDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def GreatCircleDistance(p1, p2):
    lat1 = p1[0]
    longe1 = p1[1]
    lat2 = p2[0]
    longe2 = p2[1]
    radius = 3959 #miles
    lat1_radians = math.radians(lat1)
    longe1_radians = math.radians(longe1)
    lat2_radians = math.radians(lat2)
    longe2_radians = math.radians(longe2)
    dlat = lat2_radians - lat1_radians
    dlonge = longe2_radians - longe1_radians
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.sin(dlonge/2) * math.sin(dlonge/2) * math.cos(lat1_radians) * math.cos(lat2_radians)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d

def distance(p1, p2):
    return EuclideanDistance(p1,p2) if distance_measure == 'Euclidean' else GreatCircleDistance(p1, p2)

with open(cluster_file, 'r') as f:
    lines = f.readlines()
    points = [line.rstrip('\n').split(',') for line in lines]
    points = [(float(point[0]), float(point[1]), int(point[2])) for point in points]

with open(centers_file, 'r') as f:
    lines = f.readlines()
    centers = [line.rstrip('\n').replace(')', '').replace('(', '').split(', ') for line in lines]
    centers = [(float(center[0]), float(center[1])) for center in centers]

total_error = sum([distance(centers[p[2]], p)**2 for p in points])

with open(out_file, 'w') as f:
    f.write(str(total_error))

