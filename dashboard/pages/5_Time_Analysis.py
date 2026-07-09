import streamlit as st
import plotly.express as px
import pandas as pd
from db import load_data
from utils import dashboard_sidebar

st.set_page_config(
    page_title="Time Analytics",
    page_icon="📅",
    layout="wide"
)

st.title("📅 Time Analytics")

df = load_data()

filtered_df = dashboard_sidebar(df)

# ----------------------------------------
# KPIs
# ----------------------------------------

total_sales = filtered_df["SalesAmount"].sum()

total_profit = filtered_df["ProfitAmount"].sum()

avg_order = filtered_df["SalesAmount"].mean()

total_quantity = filtered_df["Quantity"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("💰 Revenue", f"₹{total_sales:,.0f}")
c2.metric("📈 Profit", f"₹{total_profit:,.0f}")
c3.metric("🛒 Avg Order", f"₹{avg_order:,.0f}")
c4.metric("📦 Quantity Sold", f"{total_quantity:,}")

st.divider()

# ----------------------------------------
# Monthly Revenue
# ----------------------------------------

left, right = st.columns(2)

with left:

    monthly = (
        filtered_df
        .groupby(["MonthNumber","MonthName"],as_index=False)["SalesAmount"]
        .sum()
        .sort_values("MonthNumber")
    )

    fig = px.line(
        monthly,
        x="MonthName",
        y="SalesAmount",
        markers=True,
        title="📈 Monthly Revenue"
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    quarterly = (
        filtered_df
        .groupby("QuarterNumber",as_index=False)["SalesAmount"]
        .sum()
    )

    fig = px.bar(
        quarterly,
        x="QuarterNumber",
        y="SalesAmount",
        title="📅 Quarterly Revenue"
    )

    st.plotly_chart(fig,use_container_width=True)

# ----------------------------------------
# Yearly Revenue
# ----------------------------------------

left,right = st.columns(2)

with left:

    yearly = (
        filtered_df
        .groupby("YearNumber",as_index=False)["SalesAmount"]
        .sum()
    )

    fig = px.bar(
        yearly,
        x="YearNumber",
        y="SalesAmount",
        title="📊 Yearly Revenue"
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    weekend = (
        filtered_df
        .groupby("IsWeekend",as_index=False)["SalesAmount"]
        .sum()
    )

    weekend["IsWeekend"] = weekend["IsWeekend"].map({
        0:"Weekday",
        1:"Weekend"
    })

    fig = px.pie(
        weekend,
        values="SalesAmount",
        names="IsWeekend",
        hole=.5,
        title="🌞 Weekend vs Weekday"
    )

    st.plotly_chart(fig,use_container_width=True)

# ----------------------------------------
# Running Revenue
# ----------------------------------------

running = (
    filtered_df
    .groupby("FullDate",as_index=False)["SalesAmount"]
    .sum()
    .sort_values("FullDate")
)

running["RunningRevenue"] = running["SalesAmount"].cumsum()

fig = px.area(
    running,
    x="FullDate",
    y="RunningRevenue",
    title="📈 Running Revenue"
)

st.plotly_chart(fig,use_container_width=True)