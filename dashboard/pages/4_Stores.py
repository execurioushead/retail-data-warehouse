import streamlit as st
import plotly.express as px
from db import load_data
from utils import dashboard_sidebar

st.set_page_config(
    page_title="Store Analytics",
    page_icon="🏬",
    layout="wide"
)

st.title("🏬 Store Analytics")

df = load_data()
filtered_df = dashboard_sidebar(df)

# --------------------------------------------------------
# KPI Cards
# --------------------------------------------------------

total_stores = filtered_df["StoreID"].nunique()
regions = filtered_df["Region"].nunique()
store_types = filtered_df["StoreType"].nunique()

avg_store_revenue = (
    filtered_df.groupby("StoreID")["SalesAmount"]
    .sum()
    .mean()
)

c1, c2, c3, c4 = st.columns(4)

c1.metric("🏬 Stores", f"{total_stores:,}")
c2.metric("🌍 Regions", regions)
c3.metric("🏪 Store Types", store_types)
c4.metric("💰 Avg Store Revenue", f"₹{avg_store_revenue:,.0f}")

st.divider()

# --------------------------------------------------------
# Row 1
# --------------------------------------------------------

left, right = st.columns(2)

with left:

    region_sales = (
        filtered_df.groupby("Region", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
    )

    fig = px.bar(
        region_sales,
        x="Region",
        y="SalesAmount",
        color="Region",
        title="🌍 Revenue by Region"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    store_type = (
        filtered_df.groupby("StoreType", as_index=False)["SalesAmount"]
        .sum()
    )

    fig = px.pie(
        store_type,
        values="SalesAmount",
        names="StoreType",
        hole=0.55,
        title="🏪 Store Type Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------
# Row 2
# --------------------------------------------------------

left, right = st.columns(2)

with left:

    top_store = (
        filtered_df.groupby("StoreName", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_store,
        x="SalesAmount",
        y="StoreName",
        orientation="h",
        title="🏆 Top 10 Stores"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    store_size = (
        filtered_df.groupby("StoreSize", as_index=False)["SalesAmount"]
        .sum()
    )

    fig = px.bar(
        store_size,
        x="StoreSize",
        y="SalesAmount",
        color="StoreSize",
        title="📏 Revenue by Store Size"
    )

    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------------
# Revenue by State
# --------------------------------------------------------

state_sales = (
    filtered_df.groupby("StoreState", as_index=False)["SalesAmount"]
    .sum()
    .sort_values("SalesAmount", ascending=False)
)

fig = px.bar(
    state_sales,
    x="StoreState",
    y="SalesAmount",
    title="🗺️ Revenue by Store State"
)

st.plotly_chart(fig, use_container_width=True)