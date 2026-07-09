import streamlit as st
import plotly.express as px
from db import load_data
from utils import dashboard_sidebar

st.set_page_config(
    page_title="Payment Analytics",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Payment Analytics")

df = load_data()
filtered_df = dashboard_sidebar(df)

# --------------------------------------------------------
# KPI Cards
# --------------------------------------------------------

total_revenue = filtered_df["SalesAmount"].sum()
total_profit = filtered_df["ProfitAmount"].sum()
total_orders = filtered_df["SaleID"].count()
avg_order = filtered_df["SalesAmount"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", f"₹{total_revenue:,.0f}")
c2.metric("📈 Profit", f"₹{total_profit:,.0f}")
c3.metric("🛒 Orders", f"{total_orders:,}")
c4.metric("📦 Avg Order Value", f"₹{avg_order:,.0f}")

st.divider()

# --------------------------------------------------------
# Row 1
# --------------------------------------------------------

left, right = st.columns(2)

with left:

    payment_revenue = (
        filtered_df
        .groupby("PaymentMethod", as_index=False)["SalesAmount"]
        .sum()
    )

    fig = px.pie(
        payment_revenue,
        values="SalesAmount",
        names="PaymentMethod",
        hole=0.55,
        title="💳 Revenue by Payment Method"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    payment_profit = (
        filtered_df
        .groupby("PaymentMethod", as_index=False)["ProfitAmount"]
        .sum()
    )

    fig = px.bar(
        payment_profit,
        x="PaymentMethod",
        y="ProfitAmount",
        color="PaymentMethod",
        title="📈 Profit by Payment Method"
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------
# Row 2
# --------------------------------------------------------

left, right = st.columns(2)

with left:

    payment_orders = (
        filtered_df
        .groupby("PaymentMethod", as_index=False)["SaleID"]
        .count()
        .rename(columns={"SaleID": "Orders"})
    )

    fig = px.bar(
        payment_orders,
        x="PaymentMethod",
        y="Orders",
        color="PaymentMethod",
        title="🛒 Orders by Payment Method"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    payment_avg = (
        filtered_df
        .groupby("PaymentMethod", as_index=False)["SalesAmount"]
        .mean()
        .rename(columns={"SalesAmount": "AverageOrderValue"})
    )

    fig = px.bar(
        payment_avg,
        x="PaymentMethod",
        y="AverageOrderValue",
        color="PaymentMethod",
        title="📦 Average Order Value"
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------
# Daily Payment Trend
# --------------------------------------------------------

trend = (
    filtered_df
    .groupby(["FullDate", "PaymentMethod"], as_index=False)["SalesAmount"]
    .sum()
)

fig = px.line(
    trend,
    x="FullDate",
    y="SalesAmount",
    color="PaymentMethod",
    title="📅 Payment Trend Over Time"
)

st.plotly_chart(fig, use_container_width=True)