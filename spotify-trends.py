"""
This project analyzes daily global stream counts for five popular songs on Spotify between 2017 and 2018. 
It uses line plots to visualize trends in music popularity over time.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style 
sns.set_style("darkgrid")

# Load dataset
spotify_filepath = "data/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Preview the data
print("First 5 rows of the dataset:")
print(spotify_data.head())

# Initialize plot
plt.figure(figsize=(14, 6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Streams", fontsize=12)

# Plot all songs
sns.lineplot(data=spotify_data)

# Save figure
plt.tight_layout()
plt.savefig("spotify_trends.png")

plt.show()
