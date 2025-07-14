import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a clean white grid background
sns.set_style("whitegrid")

# Load the flight delay dataset
flight_data = pd.read_csv("data/flight_delays.csv", index_col="Month")

# Print the first few rows
print("Flight delay dataset (first 5 rows):")
print(flight_data.head())

# Prepare the figure
plt.figure(figsize=(10, 6))
plt.title("Average Arrival Delay for Spirit Airlines (NK) by Month", fontsize=14)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Delay (minutes)", fontsize=12)

# Create a bar chart using seaborn
sns.barplot(x=flight_data.index, y=flight_data['NK'], palette="coolwarm")

# Save and display the figure
plt.tight_layout()
plt.savefig("spirit_airlines_barplot.png")
plt.show()
