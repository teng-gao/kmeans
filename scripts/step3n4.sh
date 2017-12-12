## Step 3
# cluster synthetic location data sample_geo.txt
hadoop fs -rm -r synthetic_euc_k4
spark-submit --master local[*] kmeans_exec.py sample_geo.txt 4 Euclidean synthetic_euc_k4/centers synthetic_euc_k4/clusters tab
hadoop fs -get synthetic_euc_k4

hadoop fs -rm -r synthetic_euc_k2
spark-submit --master local[*] kmeans_exec.py sample_geo.txt 2 Euclidean synthetic_euc_k2/centers synthetic_euc_k2/clusters tab
rm -rf synthetic_euc_k2; hadoop fs -get synthetic_euc_k2

hadoop fs -rm -r synthetic_cir_k4
spark-submit --master local[*] kmeans_exec.py sample_geo.txt 4 GreatCircleDistance synthetic_cir_k4/centers synthetic_cir_k4/clusters tab
hadoop fs -get synthetic_cir_k4

hadoop fs -rm -r synthetic_cir_k2
spark-submit --master local[*] kmeans_exec.py sample_geo.txt 2 GreatCircleDistance synthetic_cir_k2/centers synthetic_cir_k2/clusters tab
hadoop fs -get synthetic_cir_k2

# visualize synthetic location data
python2.7 visualize.py synthetic_euc_k4/centers/part-00000 synthetic_euc_k4/clusters/part-00000 comma kmeans/trunk/plots/synthetic_euc_k4.png
python2.7 visualize.py synthetic_euc_k2/centers/part-00000 synthetic_euc_k2/clusters/part-00000 comma kmeans/trunk/plots/synthetic_euc_k2.png
python2.7 visualize.py synthetic_cir_k4/centers/part-00000 synthetic_cir_k4/clusters/part-00000 comma kmeans/trunk/plots/synthetic_cir_k4.png
python2.7 visualize.py synthetic_cir_k2/centers/part-00000 synthetic_cir_k2/clusters/part-00000 comma kmeans/trunk/plots/synthetic_cir_k2.png

python2.7 visualize_map.py synthetic_euc_k4/centers/part-00000 synthetic_euc_k4/clusters/part-00000 comma kmeans/trunk/plots/synthetic_euc_k4_map.png
python2.7 visualize_map.py synthetic_euc_k2/centers/part-00000 synthetic_euc_k2/clusters/part-00000 comma kmeans/trunk/plots/synthetic_euc_k2_map.png
python2.7 visualize_map.py synthetic_cir_k4/centers/part-00000 synthetic_cir_k4/clusters/part-00000 comma kmeans/trunk/plots/synthetic_cir_k4_map.png
python2.7 visualize_map.py synthetic_cir_k2/centers/part-00000 synthetic_cir_k2/clusters/part-00000 comma kmeans/trunk/plots/synthetic_cir_k2_map.png

# cluster device data
hadoop fs -rm -r device_euc_k5
spark-submit --master local[*] kmeans_exec.py device_data.txt 5 Euclidean device_euc_k5/centers device_euc_k5/clusters comma
rm -rf device_euc_k5; hadoop fs -get device_euc_k5

hadoop fs -rm -r device_cir_k5
spark-submit --master local[*] kmeans_exec.py device_data.txt 5 GreatCircleDistance device_cir_k5/centers device_cir_k5/clusters comma
rm -rf device_cir_k5; hadoop fs -get device_cir_k5

# visualize device data
python2.7 visualize.py device_euc_k5/centers/part-00000 device_euc_k5/clusters/part-00000 comma kmeans/trunk/plots/device_euc_k5.png
python2.7 visualize.py device_cir_k5/centers/part-00000 device_cir_k5/clusters/part-00000 comma kmeans/trunk/plots/device_cir_k5.png

python2.7 visualize_map.py device_euc_k5/centers/part-00000 device_euc_k5/clusters/part-00000 comma kmeans/trunk/plots/device_euc_k5_map.png
python2.7 visualize_map.py device_cir_k5/centers/part-00000 device_cir_k5/clusters/part-00000 comma kmeans/trunk/plots/device_cir_k5_map.png

# cluster DBpedia data
hadoop fs -rm -r dbpedia_euc_k6
spark-submit --master local[*] kmeans_exec.py lat_longs.txt 6 Euclidean dbpedia_euc_k6/centers dbpedia_euc_k6/clusters space
hadoop fs -get dbpedia_euc_k6

hadoop fs -rm -r dbpedia_cir_k6
spark-submit --master local[*] kmeans_exec.py lat_longs.txt 6 GreatCircleDistance dbpedia_cir_k6/centers dbpedia_cir_k6/clusters space
hadoop fs -get dbpedia_cir_k6

# visualize dbpedia data
python2.7 visualize.py dbpedia_euc_k6/centers/part-00000 dbpedia_euc_k6/clusters/part-00000 comma kmeans/trunk/plots/dbpedia_euc_k6.png
python2.7 visualize.py dbpedia_cir_k6/centers/part-00000 dbpedia_cir_k6/clusters/part-00000 comma kmeans/trunk/plots/dbpedia_cir_k6.png

python2.7 visualize_map.py dbpedia_euc_k6/centers/part-00000 dbpedia_euc_k6/clusters/part-00000 comma kmeans/trunk/plots/dbpedia_euc_k6_map.png
python2.7 visualize_map.py dbpedia_cir_k6/centers/part-00000 dbpedia_cir_k6/clusters/part-00000 comma kmeans/trunk/plots/dbpedia_cir_k6_map.png

## compare runtime of three datasets using k = 3, 3 thread
for i in 1 2 3; do hadoop fs -rm -r synthetic_euc_k3_speed; spark-submit --master local[3] kmeans_exec.py sample_geo.txt 3 Euclidean synthetic_euc_k3_speed/centers synthetic_euc_k3_speed/clusters tab; done
# local-1512972580092 Start: 2017/12/11 00:09:34 End: 2017/12/11 00:10:08

for i in 1 2 3; do hadoop fs -rm -r device_euc_k3_speed; spark-submit --master local[3] kmeans_exec.py device_data.txt 3 Euclidean device_euc_k3_speed/centers device_euc_k3_speed/clusters comma; done
# local-1512973117213 Start: 2017/12/11 00:18:30 End: 2017/12/11 00:20:27

for i in 1 2 3; do hadoop fs -rm -r dbpedia_euc_k3_speed; spark-submit --master local[3] kmeans_exec.py lat_longs.txt 3 Euclidean dbpedia_euc_k3_speed/centers dbpedia_euc_k3_speed/clusters space; done
# local-1512972922310 Start: 2017/12/11 00:15:15 End: 2017/12/11 00:17:30

# compare runtime of persist vs not persist
for i in 1 2 3; do hadoop fs -rm -r synthetic_euc_k3_speed_2; spark-submit --master local[3] kmeans_exec_nopersist.py sample_geo.txt 3 Euclidean synthetic_euc_k3_speed_2/centers synthetic_euc_k3_speed_2/clusters tab; done
# local-1512973329079 Start: 2017/12/11 00:22:02 End: 2017/12/11 00:22:30

for i in 1 2 3; do hadoop fs -rm -r device_euc_k3_speed_2; spark-submit --master local[3] kmeans_exec_nopersist.py device_data.txt 3 Euclidean device_euc_k3_speed_2/centers device_euc_k3_speed_2/clusters comma; done
# local-1512973361493 Start: 2017/12/11 00:22:35 End: 2017/12/11 00:24:46

for i in 1 2 3; do hadoop fs -rm -r dbpedia_euc_k3_speed_2; spark-submit --master local[3] kmeans_exec_nopersist.py lat_longs.txt 3 Euclidean dbpedia_euc_k3_speed_2/centers dbpedia_euc_k3_speed_2/clusters space; done
# local-1512973498778 Start: 2017/12/11 00:24:51 End: 2017/12/11 00:30:09
