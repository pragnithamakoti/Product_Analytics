import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Product Analytics Dashboard", layout="wide")
st.title("📊 Product Analytics Dashboard")

# -----------------------------
# DEBUG SECTION (VERY IMPORTANT)
# -----------------------------
st.subheader("🔍 Debug Info")

root_files = os.listdir()
st.write("ROOT FILES:", root_files)

if os.path.exists('data'):
    data_files = os.listdir('data')
    st.write("DATA FOLDER FILES:", data_files)
else:
    st.error("❌ 'data' folder NOT FOUND")

# -----------------------------
# AUTO DETECT CSV FILE (NO ERROR)
# -----------------------------
df = None

if os.path.exists('data'):
    for file in os.listdir('data'):
        if file.endswith('.csv'):
            file_path = os.path.join('data', file)
            st.success(f"✅ Using file: {file}")
            df = pd.read_csv(file_path)
            break

if df is None:
    st.error("❌ No CSV file found in data folder")
    st.stop()

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🔍 Filters")

membership = st.sidebar.multiselect(
    "Select Membership Type",
    df['Membership Type'].unique(),
    default=df['Membership Type'].unique()
)

age_range = st.sidebar.slider(
    "Select Age Range",
    int(df['Age'].min()),
    int(df['Age'].max()),
    (int(df['Age'].min()), int(df['Age'].max()))
)

spend_range = st.sidebar.slider(
    "Select Spend Range",
    int(df['Total Spend'].min()),
    int(df['Total Spend'].max()),
    (int(df['Total Spend'].min()), int(df['Total Spend'].max()))
)

# Apply filters
filtered_df = df[
    (df['Membership Type'].isin(membership)) &
    (df['Age'].between(age_range[0], age_range[1])) &
    (df['Total Spend'].between(spend_range[0], spend_range[1]))
]

# -----------------------------
# KPIs
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Revenue", f"{filtered_df['Total Spend'].sum():.2f}")
col2.metric("👥 Customers", filtered_df['Customer ID'].nunique())
col3.metric("📈 Avg Spend", f"{filtered_df['Total Spend'].mean():.2f}")

# -----------------------------
# Customer Search
# -----------------------------
st.subheader("🔎 Search Customer")

customer_id = st.text_input("Enter Customer ID")

if customer_id:
    result = filtered_df[filtered_df['Customer ID'].astype(str) == customer_id]
    st.dataframe(result)

# -----------------------------
# Revenue by Membership
# -----------------------------
st.subheader("📊 Revenue by Membership")

rev = filtered_df.groupby('Membership Type')['Total Spend'].sum()

fig1, ax1 = plt.subplots()
sns.barplot(x=rev.index, y=rev.values, ax=ax1)
st.pyplot(fig1)

# -----------------------------
# Satisfaction vs Spending
# -----------------------------
st.subheader("😊 Satisfaction vs Spending")

fig2, ax2 = plt.subplots()
sns.boxplot(x='Satisfaction Level', y='Total Spend', data=filtered_df, ax=ax2)
st.pyplot(fig2)

# -----------------------------
# Top Customers
# -----------------------------
st.subheader("🏆 Top Customers")

top_customers = filtered_df.sort_values(by='Total Spend', ascending=False).head(10)
st.dataframe(top_customers)

# -----------------------------
# Download Data
# -----------------------------
st.subheader("📥 Download Filtered Data")

csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Download CSV",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("✅ Product Analytics Dashboard")
