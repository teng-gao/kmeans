# visualization
import matplotlib.pyplot as plt
import numpy as np
import sys

#Usage: python2.7 visualize.py <centers file> <clusters file> <out file>

centers_file = str(sys.argv[1])
clusters_file = str(sys.argv[2])
out_file = str(sys.argv[4])

# centers_file = 'synthetic_euc_k2/centers/part-00000'; clusters_file = 'synthetic_euc_k2/clusters/part-00000'

# set seperator
if str(sys.argv[3]).lower() == 'tab':
    sep = '\t'
elif str(sys.argv[3]).lower() == 'comma':
    sep = ','
else:
    sep = ' '

# set color dict
color_dict = {0:'aqua', 1:'olivedrab', 2: 'palegreen', 3: 'cornflowerblue', 4: 'orchid', 5: 'goldenrod', 6: 'seagreen', 7: 'salmon'}

# read in final center data
with open(centers_file, 'r') as f:
    lines = [line.rstrip('\n').replace('(', '').replace(')', '').split(sep) for line in f.readlines()]
    lines = [line for line in lines if line[0] not in ['\n','']]
    final_centers = [(float(points[0]), float(points[1])) for points in lines]

# read in final cluster data
with open(clusters_file, 'r') as f:
    lines = [line.rstrip('\n').split(sep) for line in f.readlines()]
    lines = [line for line in lines if line[0] not in ['\n','']]
    # if too big, random sample
    if len(lines) > 20000:
        inds = list(np.random.choice(len(lines), 20000, replace=False))
        lines = [lines[i] for i in inds]
    points = [(float(points[0]), float(points[1])) for points in lines]
    colors = [color_dict[int(point[2])] for point in lines]

# scatter points and centers
plt.scatter([p[1] for p in points], [p[0] for p in points], marker='o', color=colors, s=4)
plt.scatter([c[1] for c in final_centers], [c[0] for c in final_centers], marker='x', s=80, facecolors='r', edgecolors='b')
# plt.scatter([c[0] for c in initial_centers], [c[1] for c in initial_centers], marker='o', s=80, facecolors='b', edgecolors='b')

plt.ylabel('Latitude')
plt.xlabel('Longtitude')

# axes = plt.gca()
# axes.set_xlim([-180, 180])
# axes.set_ylim([-180, 180])
# plt.show()
plt.savefig(out_file, dpi = 300)
