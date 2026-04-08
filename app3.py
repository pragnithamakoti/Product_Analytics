import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="Product Analytics Dashboard", layout="wide")
st.title("📊 Product Analytics Dashboard")
try:
   df = pd.read_csv('../data/ecommerce_data.csv')
except:
    st.error("❌ File not found. Check your file path!")
    st.stop()
df.columns = df.columns.str.strip()  
st.subheader("📄 Dataset Preview")
st.write(df.head())
st.subheader("🧾 Column Names")
st.write(df.columns)
st.subheader("📊 Dataset Info")
st.write(df.describe())
st.subheader("📈 Data Visualization")
col1, col2 = st.columns(2)
with col1:
    fig1, ax1 = plt.subplots()
    if 'Gender' in df.columns:
        sns.countplot(x='Gender', data=df, ax=ax1)
        ax1.set_title("Gender Distribution")
        st.pyplot(fig1)
    else:
        st.warning("⚠️ 'Gender' column not found")
with col2:
    fig2, ax2 = plt.subplots()
    if 'Customer Type' in df.columns:
        sns.countplot(x='Customer Type', data=df, ax=ax2)
        ax2.set_title("Customer Type Distribution")
        st.pyplot(fig2)
    else:
        st.warning("⚠️ 'Customer Type' column not found")
st.subheader("📦 Category Analysis")
if 'Category' in df.columns:
    fig3, ax3 = plt.subplots()
    sns.countplot(x='Category', data=df, ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)
else:
    st.info("ℹ️ 'Category' column not available")
st.markdown("---")
st.write("✅ Dashboard Loaded Successfully!")