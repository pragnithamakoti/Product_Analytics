# 01_data_exploration.py
# Day 1: Product Analytics - Data Loading & Exploration

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===============================
# Step 0: Set file path
# ===============================
file_path = "data/ecommerce_data.csv"  # Make sure your CSV is in 'data/' folder

# Check if file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"CSV file not found! Please place it here: {file_path}")

# ===============================
# Step 1: Load Dataset
# ===============================
df = pd.read_csv(file_path)
print("=== Dataset Loaded Successfully ===\n")

# ===============================
# Step 2: Basic Dataset Info
# ===============================
print("=== First 5 Rows ===")
print(df.head(), "\n")

print("=== Dataset Info ===")
print(df.info(), "\n")

print("=== Missing Values per Column ===")
print(df.isnull().sum(), "\n")

# ===============================
# Step 3: Basic Statistics
# ===============================
total_customers = df['Customer ID'].nunique()  # corrected column
total_events = len(df)
event_counts = df['Membership Type'].value_counts()  # example categorical column

print(f"Total Customers: {total_customers}")
print(f"Total Records: {total_events}")
print("Membership Type Distribution:")
print(event_counts, "\n")

# ===============================
# Step 4: Data Cleaning
# ===============================
# Convert columns if needed (example: Age is already int)
# Convert Days Since Last Purchase to numeric if not already
df['Days Since Last Purchase'] = pd.to_numeric(df['Days Since Last Purchase'], errors='coerce')

# Drop rows with missing values
df = df.dropna()

# Drop duplicate rows
df = df.drop_duplicates()

print("=== Data Cleaning Completed ===\n")

# ===============================
# Step 5: Simple Visualization
# ===============================
plt.figure(figsize=(8,5))
sns.countplot(x='Membership Type', data=df)
plt.title("Membership Type Distribution")
plt.xlabel("Membership Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ===============================
# Step 6: Save Cleaned Dataset
# ===============================
cleaned_file_path = "data/cleaned_data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved as '{cleaned_file_path}'")