import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Load iris flower dataset
iris_data = pd.read_csv("data/iris.csv", index_col="Id")

# Show first rows
print("First 5 rows of the iris dataset:")
print(iris_data.head())

# Histogram for Petal Length by Species
plt.figure(figsize=(10, 6))
sns.histplot(data=iris_data, x="Petal Length (cm)", hue="Species", multiple="stack", kde=False)
plt.title("Histogram of Petal Lengths by Species", fontsize=14)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.savefig("iris_histogram.png")
plt.show()

# KDE Plot for Petal Length by Species
plt.figure(figsize=(10, 6))
sns.kdeplot(data=iris_data, x="Petal Length (cm)", hue="Species", fill=True)
plt.title("KDE of Petal Lengths by Species", fontsize=14)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Density")
plt.savefig("iris_kde.png")
plt.show()

