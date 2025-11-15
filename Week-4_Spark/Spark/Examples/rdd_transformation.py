from pyspark.sql import SparkSession

import sys
import os
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-18.0.1.1"
os.environ['HADOOP_HOME'] = "C:/hadoop"
os.environ["SPARK_HOME"] = "D:/Revature_Training/Week-4_Spark/Spark/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .appName("Local PySpark") \
    .getOrCreate()

#Get SparkContext
sc = spark.sparkContext
'''
numbers = [1,2,3,4,5]
rdd = sc.parallelize(numbers)
print("Original RDD: ", rdd.collect())



#Transformations
doubled = rdd.map(lambda x: x * 2)
print('type : ', type(doubled))
print("Doubled: ", doubled.collect())

even_num= rdd.filter(lambda x: x%2==0)
print('type : ', type(even_num))
print("Even num: ", even_num.collect())

total = rdd.reduce(lambda x, y: x + y)
print('type : ', type(total))
print("Total Sum: ", total)


#
lines = sc.parallelize(["hello world","Hello spark","Hello Rdd"])
words = lines.flatMap(lambda line: line.split(" "))
print("Words: ", words.collect())
word_pairs = words.map(lambda word: (word, 1))
print("Word pairs: ", word_pairs.collect())
word_counts = word_pairs.reduceByKey(lambda x, y: x + y)
print("Word counts: ", word_counts.collect())

data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, ["Name","Age"])
df.show()'''




stopwords = ["is", "a", "the", "and", "of"]
b_stop = spark.sparkContext.broadcast(stopwords)

rdd = spark.sparkContext.textFile("../data/article.txt")
words = rdd.flatMap(lambda x: x.lower().split())
filtered = words.filter(lambda w: w not in b_stop.value)
pairs = filtered.map(lambda w: (w, 1))
wordCount = pairs.reduceByKey(lambda a, b: a + b)
print(wordCount.collect())

wordCount.saveAsTextFile("../output/wordcount")

