# Source: http://maxberggren.se/2015/08/04/basemap/
import matplotlib.pyplot as plt
import numpy as np
import sys
from mpl_toolkits.basemap import Basemap

#Usage: python2.7 visualize.py <centers file> <clusters file> <out file> <title>

centers_file = str(sys.argv[1])
clusters_file = str(sys.argv[2])
out_file = str(sys.argv[4])
# title = str(sys.argv[5])

# centers_file = 'dbpedia_euc_k6/centers/part-00000'; clusters_file = 'dbpedia_euc_k6/clusters/part-00000'; sep = ','
# centers_file = 'synthetic_euc_k4/centers/part-00000'; clusters_file = 'synthetic_euc_k4/clusters/part-00000'; sep = ','
# centers_file = 'device_euc_k5/centers/part-00000'; clusters_file = 'device_euc_k5/clusters/part-00000'; sep = ','

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
    if len(lines) > 50000:
        inds = list(np.random.choice(len(lines), 50000, replace=False))
        lines = [lines[i] for i in inds]
    points = [(float(points[0]), float(points[1])) for points in lines]
    colors = [color_dict[int(point[2])] for point in lines]

# calculate coordinates for points, create basemap, determine region
points_lat = [p[0] for p in points]
points_long = [p[1] for p in points]

if min(points_lat) > 24 and max(points_lat) < 50:
    m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    m.drawstates()
    m.drawcoastlines()
    m.drawcountries()
    center_size = 80
    center_lw = '2'

# elif -125 < min(points_long) and max(points_long) < -108:
#     m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
#         projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
#     m.drawstates()
#     m.drawcoastlines()
#     m.drawcountries()
else:
    m = Basemap(resolution='c', projection='kav7', lat_0=0., lon_0=0.)
    n_graticules = 18
    parallels = np.arange(-80., 90, n_graticules)
    meridians = np.arange(0., 360., n_graticules)
    lw = 1
    dashes = [5,7] # 5 dots, 7 spaces... repeat
    graticules_color = 'grey'

    fig1 = plt.figure(figsize=(16,20))
    fig1.patch.set_facecolor('#e6e8ec')
    ax = fig1.add_axes([0.1,0.1,0.8,0.8])

    m.drawmapboundary(color='white',
                      linewidth=0.0,
                      fill_color='white')
    m.drawparallels(parallels,
                    linewidth=lw,
                    dashes=dashes,
                    color=graticules_color)
    m.drawmeridians(meridians,
                    linewidth=lw,
                    dashes=dashes,
                    color=graticules_color)
    m.drawcoastlines(linewidth=0)
    m.fillcontinents('black',
                     lake_color='white')
    m.drawcountries(linewidth=1,
                    linestyle='solid',
                    color='white',
                    zorder=30)
    center_size = 300
    center_lw = '5'

# title = plt.title(title, fontsize=20)
# title.set_y(1.03)

# Convert points and centers coords to projected place in figure
x_points, y_points = m(points_long, points_lat)
x_centers, y_centers = m([c[1] for c in final_centers], [c[0] for c in final_centers])

# scatter points and center
m.scatter(x_points, y_points,
          s=4,
          marker="o",
          color=colors,
          zorder=10,
          alpha=1)

m.scatter(x_centers, y_centers, marker='x', linewidth=center_lw, s=center_size, facecolors='r', edgecolors='b', zorder=10, alpha=1)

plt.savefig(out_file, dpi = 300)
