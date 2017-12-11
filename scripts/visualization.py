# visualization
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d


final_centers_pedia = [(26.263288914910653, 71.5174887880303),
(47.96503198863253, 10.600638329100747),
(42.37736888079699, -116.5799122261968),
(34.1863266882007, -81.40779807259366)]

final_centers_synthetic_euc_k2 = [(37.56474719519914, -82.55711081529088), (38.07161548087938, -116.43342043085099)]

final_centers = final_centers_synthetic_euc_k2
# read in sample data and parse
input_file = 'sample_geo.txt'; sep = '\t'
input_file = 'synthetic_euc_k2/clusters/part-00000'; sep = ','
color_dict = {0:'salmon', 1:'olivedrab', 2: 'palegreen', 3: 'cornflowerblue', 4: 'orchid', 5: 'fuchsia', 6: 'seagreen', 7: 'aqua'}

with open(input_file, 'r') as f:
    lines = [line.rstrip('\n').split(sep) for line in f.readlines()]
    lines = [line for line in lines if line[0] not in ['\n','']]
    points = [(float(points[0]), float(points[1])) for points in lines]
    colors = [color_dict[int(point[2])] for point in lines]

# voronoi plot using final center
# vor = Voronoi(final_centers)
# voronoi_plot_2d(vor)

# scatter points and centers
plt.scatter([p[1] for p in points], [p[0] for p in points], marker='x', color=colors)
plt.scatter([c[1] for c in final_centers], [c[0] for c in final_centers], marker='o', s=80, facecolors='r', edgecolors='b')
# plt.scatter([c[0] for c in initial_centers], [c[1] for c in initial_centers], marker='o', s=80, facecolors='b', edgecolors='b')

axes = plt.gca()
# axes.set_xlim([-180, 180])
# axes.set_ylim([-180, 180])
# plt.show()
plt.savefig('synthetic_euc_k2.png')
