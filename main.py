import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Movies", "TV Shows"],
    "Count": [6131, 2676]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df["Category"], df["Count"])
plt.title("Movies vs TV Shows")
plt.xlabel("Category")
plt.ylabel("Count")
plt.savefig("movies_vs_tvshows.png")

print("Visualization created successfully")
