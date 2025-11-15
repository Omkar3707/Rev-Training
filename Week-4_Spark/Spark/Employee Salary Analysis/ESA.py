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


data = [
    (101,"Alice","HR",3500),
    (102,"Bob","IT",4200),
    (103,"Cathie","Finance",3900),
    (104,"David","IT",4900),
    (105,"Edward","HR",5200)
]
column=["id","ename","dept","salary"]

emp_df=spark.createDataFrame(data,column)
emp_df.createOrReplaceTempView("employees")


# 1. Aggregations
agg_df = spark.sql("""
   SELECT Dept, 
          COUNT(*) AS Count,
          AVG(Salary) AS Avg_Salary,
          SUM(Salary) AS Total_Salary
   FROM employees
   GROUP BY Dept
""")
agg_df.show()

# 2. Employees above average
high_earners = spark.sql("""
   SELECT e.ename, e.Dept, e.Salary
   FROM employees e
   JOIN (
       SELECT Dept, AVG(Salary) AS Avg_Salary FROM employees GROUP BY Dept
   ) d
   ON e.Dept = d.Dept
   WHERE e.Salary > d.Avg_Salary
""")
high_earners.show()

# 3. Save results
#high_earners.write.mode("overwrite").parquet("../output/high_earners")

