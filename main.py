import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualization
plt.figure(figsize=(6,4))
df["species"].value_counts().plot(kind="bar")
plt.title("Count of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.savefig("iris_species.png")

print("Project Completed Successfully")
