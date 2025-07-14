import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("dark")

# Load insurance dataset
insurance_data = pd.read_csv("data/insurance.csv")

# Preview
print("First 5 rows of insurance data:")
print(insurance_data.head())

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
plt.title("BMI vs Insurance Charges (with Regression Line)")
sns.regplot(x="bmi", y="charges", data=insurance_data, scatter_kws={'alpha':0.5})
plt.xlabel("Body Mass Index (BMI)")
plt.ylabel("Insurance Charges")
plt.savefig("regplot_bmi_charges.png")
plt.show()

# Colored scatter by smoking status
plt.figure(figsize=(10, 6))
sns.scatterplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
plt.title("BMI vs Charges Colored by Smoking Status")
plt.savefig("scatter_smoker.png")
plt.show()

# Regression lines per group (smokers vs non-smokers)
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data, aspect=1.5)
plt.title("BMI vs Charges Regression (Grouped by Smoking Status)")
plt.savefig("lmplot_bmi_smoker.png")
plt.show()

