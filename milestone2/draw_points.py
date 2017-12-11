import gmplot

latitudes = []
longitudes = []

# latitudes.append(40.9137)
# longitudes.append(-73.9536)

# latitudes.append(40.91407)
# longitudes.append(-73.95887)

f = open('sample_geo.txt','r')
for line in f:
	#line = f.readLine()
	#if line is None: break
	line_prts = line.split()
	lat = line_prts[0]
	longe = line_prts[1]
	latitudes.append(float(lat))
	longitudes.append(float(longe))

gmap = gmplot.GoogleMapPlotter(latitudes[0],longitudes[0], 16)
#gmap.scatter(latitudes, longitudes, '#FF6666', edge_width=10)
#gmap.scatter(latitudes, longitudes, 'cornflowerblue', edge_width=4)
gmap.scatter(latitudes, longitudes, '#8A0707', size=10000, marker=False)

#gmap.heatmap(latitudes, longitudes)

gmap.draw('map2.html') 
