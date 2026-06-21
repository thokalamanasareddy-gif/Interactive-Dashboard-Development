# app.py

import streamlit as st # type: ignore
import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

st.title("Interactive Sales Dashboard")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", f"₹{total_sales:,}")

with col2:
    st.metric("Total Profit", f"₹{total_profit:,}")

fig1 = px.bar(
    df,
    x="Product",
    y="Sales",
    title="Sales by Product"
)

st.plotly_chart(fig1)

fig2 = px.line(
    df,
    x="Date",
    y="Sales",
    title="Sales Trend"
)

st.plotly_chart(fig2)

st.subheader("Insights")

st.write("""
1. Laptop has highest sales.
2. Sales trend can be monitored daily.
3. Dashboard helps management make decisions.
""")