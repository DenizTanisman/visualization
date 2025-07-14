import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use tick-style grid background
sns.set_style("ticks")

# Load the full dataset
flight_data = pd.read_csv("data/flight_delays.csv", index_col="Month")

# Show entire dataset in console
print("Complete flight delay dataset:")
print(flight_data)

# Plot a heatmap
plt.figure(figsize=(14, 8))
plt.title("Average Monthly Arrival Delays by Airline (2015)", fontsize=15)

# Create the heatmap
sns.heatmap(data=flight_data, annot=True, fmt=".1f", cmap="YlOrBr", linewidths=0.5)

# Customize axis labels
plt.xlabel("Airline Code")
plt.ylabel("Month")

# Save and show the heatmap
plt.tight_layout()
plt.savefig("airline_delay_heatmap.png")
plt.show()
