import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_csv("sales_data.csv")

# 2. Basic Info
print("First 5 rows:\n", data.head())
print("\nDataset Info:")
print(data.info())
print("\nSummary Stats:\n", data.describe())

# 3. Check missing values
print("\nMissing Values:\n", data.isnull().sum())

# 4. Total sales by product
sales_by_product = data.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Product:\n", sales_by_product)

# 5. Total sales by region
sales_by_region = data.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", sales_by_region)

# 6. Monthly trend
data["Date"] = pd.to_datetime(data["Date"])
monthly_sales = data.groupby(data["Date"].dt.to_period("M"))["Sales"].sum()

# 7. Visualizations
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
