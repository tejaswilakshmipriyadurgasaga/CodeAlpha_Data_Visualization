import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("books_dataset.csv")

os.makedirs("graphs", exist_ok=True)

rating_order = ["One", "Two", "Three", "Four", "Five"]

rating_numeric = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_numeric)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
avg_price = df.groupby("Rating")["Price (INR)"].mean().reindex(rating_order)
sns.barplot(x=avg_price.index, y=avg_price.values)
plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (INR)")
plt.tight_layout()
plt.savefig("graphs/average_price_rating.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Rating", order=rating_order)
plt.title("Number of Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("graphs/rating_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df["Price (INR)"], bins=15, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (INR)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("graphs/price_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Rating", y="Price (INR)", order=rating_order)
plt.title("Book Price Variation by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (INR)")
plt.tight_layout()
plt.savefig("graphs/price_rating_boxplot.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Rating_Number", y="Price (INR)", hue="Rating", s=80)
plt.title("Relationship Between Book Rating and Price")
plt.xlabel("Rating")
plt.ylabel("Price (INR)")
plt.tight_layout()
plt.savefig("graphs/price_rating_scatter.png", dpi=300)
plt.show()

print("Task 3 completed successfully!")
print("\nDataset Shape:", df.shape)
print("\nAverage Price by Rating:")
print(avg_price)
print("\nRating Distribution:")
print(df["Rating"].value_counts())