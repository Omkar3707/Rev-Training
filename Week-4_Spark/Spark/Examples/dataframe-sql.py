from pyspark.sql import SparkSession

import sys
import os
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-18.0.1.1"
os.environ["SPARK_HOME"] = "D:/Revature_Training/Week-4_Spark/Spark/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder \
    .appName("Local PySpark") \
    .getOrCreate()

#Get SparkContext
sc = spark.sparkContext


'''data = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
df = spark.createDataFrame(data, ["Name","Age"])
df.show()

df.select("Name").show()
df.filter(df.Age > 25).show()
df.groupBy("Age").count().show()
df.orderBy(df.Age.desc()).show()

from pyspark.sql.functions import col,upper
df.select(upper(col("Name")).alias("NAME_UPPER")).show()'''

'''from pyspark.sql.types import StructType, StructField, StringType, IntegerType

myschema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    #StructField("_corrupt_record", StringType(), True),
])
#df = spark.read.option("multiline","true").json("../data/file1.json", schema = myschema)
df = spark.read.json("../data/file1.json", schema = myschema)
df.cache()
df_cleaned = df.filter("name is not null and  age is not null")
df_cleaned.show()
df.show()
df.printSchema()

df.createOrReplaceTempView("people")
spark.sql("select name from people where age > 25").show()
'''
#df.write.json("../data/out1.json")

data = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
columns = ["name", "age"]

df = spark.createDataFrame(data, columns)
df.show()
df.write.mode("overwrite").parquet("../data/file2.parquet")
df = spark.read.parquet("../data/file2.parquet")
df.show()