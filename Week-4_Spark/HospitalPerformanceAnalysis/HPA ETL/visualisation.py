# STEP 5: Convert to Pandas for Visualization
import pandas as pd

avg_cost_pd = pd.read_csv("../output-data/avg_cost_per_hospital.csv")
avg_days_pd = pd.read_csv("../output-data/avg_days_by_diagnosis.csv")
rating_cost_pd = pd.read_csv("../output-data/rating_vs_cost.csv")

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
