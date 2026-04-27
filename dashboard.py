import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("📊 INTERACTIVE SALES DASHBOARD")
print("-" * 40)

# Load data
df = pd.read_csv("sales_data.csv")

print("\nFirst 5 Rows:")
print(df.head())

# Total sales
if "Total_Sales" not in df.columns:
    df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nTotal Revenue:", df["Total_Sales"].sum())

# Style
sns.set(style="darkgrid")

# 1 Bar chart
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Total_Sales", data=df)
plt.title("Product Sales")
plt.tight_layout()
plt.savefig("sales_bar.png")
plt.close()

# 2 Pie chart
region = df.groupby("Region")["Total_Sales"].sum()
plt.figure(figsize=(6,6))
plt.pie(region, labels=region.index, autopct="%1.1f%%")
plt.title("Region Sales")
plt.savefig("sales_pie.png")
plt.close()

# 3 Heatmap
corr = df[["Quantity","Price","Total_Sales"]].corr()
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("sales_heatmap.png")
plt.close()

# 4 Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x="Product", y="Price", data=df)
plt.title("Price Distribution")
plt.tight_layout()
plt.savefig("sales_boxplot.png")
plt.close()

print("\n✅ Charts created successfully")
print("✅ Dashboard Project Completed")