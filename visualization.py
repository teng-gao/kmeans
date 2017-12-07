# visualization
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# final_centers = [(-3.3317347701149425, -62.14183170498081),
#  (43.22474153743314, 10.419616617548034),
#  (19.62659117762128, 104.22780737480441),
#  (37.821261279683874, -96.58667536271501)]
final_centers = [(26.263288914910653, 71.5174887880303),
(47.96503198863253, 10.600638329100747),
(42.37736888079699, -116.5799122261968),
(34.1863266882007, -81.40779807259366)]

# read in sample data and parse
with open('lat_longs.txt', 'r') as f:
    points = [(float(points[0]), float(points[1])) for points in [line.split(' ') for line in f.readlines()]]

# voronoi plot using final center
vor = Voronoi(final_centers)
voronoi_plot_2d(vor)

# scatter points and centers
plt.scatter([p[0] for p in points], [p[1] for p in points], marker='x')
plt.scatter([c[0] for c in final_centers], [c[1] for c in final_centers], marker='o', s=80, facecolors='r', edgecolors='r')
plt.scatter([c[0] for c in initial_centers], [c[1] for c in initial_centers], marker='o', s=80, facecolors='b', edgecolors='b')

axes = plt.gca()
axes.set_xlim([-180, 180])
axes.set_ylim([-180, 180])
plt.show()
