# Day 3: Advanced Product Analytics & User Behaviour Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load Cleaned Dataset
# -----------------------------
df = pd.read_csv('data/cleaned_data.csv')

print("=== Dataset Loaded ===")
print(df.head())

# -----------------------------
# Step 2: Feature Engineering
# -----------------------------

# Spend per item
df['Spend per Item'] = df['Total Spend'] / df['Items Purchased']

# Customer Type based on recency
df['Customer Type'] = df['Days Since Last Purchase'].apply(lambda x:
    'Active' if x <= 20 else
    'Regular' if x <= 40 else
    'Inactive'
)

print("\n=== New Features Created ===")
print(df[['Spend per Item', 'Customer Type']].head())

# -----------------------------
# Step 3: Customer Segmentation
# -----------------------------

# Average spend by membership
membership_spend = df.groupby('Membership Type')['Total Spend'].mean()

print("\n=== Average Spend by Membership Type ===")
print(membership_spend)

# Customer type distribution
customer_type_count = df['Customer Type'].value_counts()

print("\n=== Customer Type Distribution ===")
print(customer_type_count)

# -----------------------------
# Step 4: Revenue Analysis
# -----------------------------

# Total revenue
total_revenue = df['Total Spend'].sum()
print("\n=== Total Revenue ===")
print(total_revenue)

# Revenue by membership
revenue_by_membership = df.groupby('Membership Type')['Total Spend'].sum()

print("\n=== Revenue by Membership Type ===")
print(revenue_by_membership)

# -----------------------------
# Step 5: Satisfaction vs Spending
# -----------------------------

satisfaction_spend = df.groupby('Satisfaction Level')['Total Spend'].mean()

print("\n=== Avg Spend by Satisfaction Level ===")
print(satisfaction_spend)

# -----------------------------
# Step 6: Visualizations
# -----------------------------

# Revenue by Membership
plt.figure(figsize=(6,4))
sns.barplot(x=revenue_by_membership.index, y=revenue_by_membership.values)
plt.title("Revenue by Membership Type")
plt.xlabel("Membership Type")
plt.ylabel("Total Revenue")
plt.show()

# Customer Segmentation
plt.figure(figsize=(6,4))
sns.countplot(x='Customer Type', data=df)
plt.title("Customer Segmentation (Active / Regular / Inactive)")
plt.xlabel("Customer Type")
plt.ylabel("Count")
plt.show()

# Satisfaction vs Spend
plt.figure(figsize=(6,4))
sns.barplot(x='Satisfaction Level', y='Total Spend', data=df)
plt.title("Satisfaction vs Spending")
plt.xlabel("Satisfaction Level")
plt.ylabel("Average Spend")
plt.show()

# Spend per Item Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Spend per Item'], kde=True)
plt.title("Spend per Item Distribution")
plt.xlabel("Spend per Item")
plt.show()

# -----------------------------
# Step 7: Top Customers
# -----------------------------

top_customers = df[['Customer ID', 'Total Spend']]\
    .sort_values(by='Total Spend', ascending=False)\
    .head(10)

print("\n=== Top 10 Customers ===")
print(top_customers)

# Save top customers
top_customers.to_csv('reports/top_customers_day3.csv', index=False)

# -----------------------------
# Step 8: Save Final Dataset
# -----------------------------

df.to_csv('data/final_analysis_data.csv', index=False)

print("\n✅ Day 3 Completed Successfully!")
print("📁 Files Saved:")
print("- data/final_analysis_data.csv")
print("- reports/top_customers_day3.csv")