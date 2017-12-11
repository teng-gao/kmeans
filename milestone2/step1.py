from pyspark import SparkContext

def reformatArr(arr):
	arr2 = []
	arr2.append(arr[12])
	arr2.append(arr[13])
	arr2.append(arr[0])
	arr2.append(arr[1])
	arr2.append(arr[2])
	return arr2

def latAndLongNot0(arr):
	return not (arr[0] == "0" and arr[1] == "0")

def splitModel(arr):
	model = arr[3].split()
	temp = arr[4]
	arr[3] = model[0]
	arr[4] = model[1]
	arr.append(temp)
	return arr

def arrToStr(arr):
	str = ""
	for x in range(0, len(arr)):
		str += arr[x]
		if x != (len(arr) - 1):
			str += ","
	return str

sc = SparkContext()
devices = sc.textFile("file:///home/training/training_materials/dev1/data/devicestatus.txt") \
	.map(lambda line :
		line.replace('|', ',').replace('/', ',').split(',')
	) \
	.filter(lambda arr : len(arr) == 14) \
	.map(lambda arr : reformatArr(arr)) \
	.filter(lambda arr : latAndLongNot0(arr)) \
	.map(lambda arr : splitModel(arr)) \
	.map(lambda arr : arrToStr(arr))

devices.saveAsTextFile("loudacre/devicestatus_etl")


#print devices
#print devices[0]
