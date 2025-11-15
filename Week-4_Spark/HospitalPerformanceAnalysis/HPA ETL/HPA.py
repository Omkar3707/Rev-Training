

'''spark = SparkSession.builder \
    .appName("Local PySpark") \
    .getOrCreate()'''

#Get SparkContext
import shutil
import sys
import os

os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-18.0.1.1"
os.environ["SPARK_HOME"] = "D:/Revature_Training/Week-4_Spark/HospitalPerformanceAnalysis/.venv/Lib/site-packages/pyspark"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# STEP 1: Setup PySpark Session

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Hospital_Analytics").getOrCreate()

# STEP 2: Load CSVs

hospitals_df = spark.read.csv("../data/hospitals.csv", header=True, inferSchema=True)
patients_df = spark.read.csv("../data/paitents.csv", header=True, inferSchema=True)

print("Hospitals Data:")
hospitals_df.show()

print("Patients Data:")
patients_df.show()

# STEP 3: Basic Transformations
from pyspark.sql.functions import col, avg, count, round as rnd

# Join patients with hospital info
joined_df = patients_df.join(hospitals_df, on="Hospital_ID", how="inner")

# Average Treatment Cost per Hospital
avg_cost = joined_df.groupBy("Hospital_Name").agg(
    rnd(avg("Treatment_Cost"), 2).alias("Avg_Treatment_Cost"),
    count("Patient_ID").alias("Patient_Count")
)
avg_cost.show()

# Top 3 hospitals by patient load
top_hospitals = avg_cost.orderBy(col("Patient_Count").desc()).limit(3)
top_hospitals.show()

# Average Admission Days by Diagnosis
avg_days_diag = joined_df.groupBy("Diagnosis").agg(
    rnd(avg("Admission_Days"), 2).alias("Avg_Admission_Days")
)
avg_days_diag.show()

# Average Rating vs Average Cost (by State)
rating_vs_cost = joined_df.groupBy("State").agg(
    rnd(avg("Rating"), 2).alias("Avg_Rating"),
    rnd(avg("Treatment_Cost"), 2).alias("Avg_Cost")
)
rating_vs_cost.show()

# STEP 4: Save Insights
# ============================
output_dir = "../output-data"
os.makedirs(output_dir, exist_ok=True)

# clean up old outputs
for subdir in ["avg_cost_per_hospital", "avg_days_by_diagnosis", "rating_vs_cost"]:
    path = os.path.join(output_dir, subdir)
    if os.path.exists(path):
        shutil.rmtree(path)

'''try:
    avg_cost.write.mode("overwrite").csv(os.path.join(output_dir, "avg_cost_per_hospital"), header=True)
    avg_days_diag.write.mode("overwrite").csv(os.path.join(output_dir, "avg_days_by_diagnosis"), header=True)
    rating_vs_cost.write.mode("overwrite").csv(os.path.join(output_dir, "rating_vs_cost"), header=True)
    print("\n Spark CSV outputs written successfully!")
except Exception as e:'''
print("\n Spark CSV write failed — likely Hadoop issue. Falling back to Pandas.")
avg_cost.toPandas().to_csv(os.path.join(output_dir, "avg_cost_per_hospital.csv"), index=False)
avg_days_diag.toPandas().to_csv(os.path.join(output_dir, "avg_days_by_diagnosis.csv"), index=False)
rating_vs_cost.toPandas().to_csv(os.path.join(output_dir, "rating_vs_cost.csv"), index=False)

# STEP 5: Convert to Pandas for Visualization

avg_cost_pd = avg_cost.toPandas()
avg_days_pd = avg_days_diag.toPandas()
rating_cost_pd = rating_vs_cost.toPandas()

# STEP 6: Visualize with Matplotlib
import matplotlib.pyplot as plt

# Plot 1: Average Treatment Cost per Hospital
plt.figure(figsize=(8, 5))
plt.bar(avg_cost_pd["Hospital_Name"], avg_cost_pd["Avg_Treatment_Cost"], color='skyblue')
plt.xticks(rotation=45, ha="right")
plt.title("Average Treatment Cost per Hospital")
plt.xlabel("Hospital Name")
plt.ylabel("Avg Treatment Cost (₹)")
plt.tight_layout()
plt.show()

# Plot 2: Average Admission Days by Diagnosis
plt.figure(figsize=(8, 5))
plt.bar(avg_days_pd["Diagnosis"], avg_days_pd["Avg_Admission_Days"], color='orange')
plt.title("Average Admission Days by Diagnosis")
plt.xlabel("Diagnosis")
plt.ylabel("Avg Admission Days")
plt.tight_layout()
plt.show()

# Plot 3: Rating vs Cost by State
plt.figure(figsize=(6, 5))
plt.scatter(rating_cost_pd["Avg_Rating"], rating_cost_pd["Avg_Cost"], color='green')
plt.title("Average Hospital Rating vs Average Treatment Cost")
plt.xlabel("Average Rating")
plt.ylabel("Average Cost (₹)")
plt.tight_layout()
plt.show()


