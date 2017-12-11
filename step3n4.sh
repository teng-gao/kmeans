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
python2.7 visualize.py synthetic_euc_k4/centers/part-00000 synthetic_euc_k4/clusters/part-00000 comma kmeans/synthetic_euc_k4.png
python2.7 visualize.py synthetic_euc_k2/centers/part-00000 synthetic_euc_k2/clusters/part-00000 comma kmeans/synthetic_euc_k2.png
python2.7 visualize.py synthetic_cir_k4/centers/part-00000 synthetic_cir_k4/clusters/part-00000 comma kmeans/synthetic_cir_k4.png
python2.7 visualize.py synthetic_cir_k2/centers/part-00000 synthetic_cir_k2/clusters/part-00000 comma kmeans/synthetic_cir_k2.png

# cluster device data
hadoop fs -rm -r device_euc_k5
spark-submit --master local[*] kmeans_exec.py device_data.txt 5 Euclidean device_euc_k5/centers device_euc_k5/clusters comma
rm -rf device_euc_k5; hadoop fs -get device_euc_k5

hadoop fs -rm -r device_cir_k5
spark-submit --master local[*] kmeans_exec.py device_data.txt 5 GreatCircleDistance device_cir_k5/centers device_cir_k5/clusters comma
rm -rf device_cir_k5; hadoop fs -get device_cir_k5

# visualize device data
python2.7 visualize.py device_euc_k5/centers/part-00000 device_euc_k5/clusters/part-00000 comma kmeans/device_euc_k5.png
python2.7 visualize.py device_cir_k5/centers/part-00000 device_cir_k5/clusters/part-00000 comma kmeans/device_cir_k5.png

# cluster DBpedia data
hadoop fs -rm -r dbpedia_euc_k6
spark-submit --master local[*] kmeans_exec.py lat_longs.txt 6 Euclidean dbpedia_euc_k6/centers dbpedia_euc_k6/clusters space
hadoop fs -get dbpedia_euc_k6

hadoop fs -rm -r dbpedia_cir_k6
spark-submit --master local[*] kmeans_exec.py lat_longs.txt 6 GreatCircleDistance dbpedia_cir_k6/centers dbpedia_cir_k6/clusters space
hadoop fs -get dbpedia_cir_k6

# visualize dbpedia data
python2.7 visualize.py dbpedia_euc_k6/centers/part-00000 dbpedia_euc_k6/clusters/part-00000 comma kmeans/dbpedia_euc_k6.png
python2.7 visualize.py dbpedia_cir_k6/centers/part-00000 dbpedia_cir_k6/clusters/part-00000 comma kmeans/dbpedia_cir_k6.png
