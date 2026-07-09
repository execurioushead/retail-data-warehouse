"""
==========================================================
Retail Sales Analytics Platform
Customer Analytics Dashboard
==========================================================
"""

import streamlit as st
import pandas as pd

from config import (
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE
)

from db import (
    load_data,
    last_refresh
)

from utils import (
    dashboard_sidebar,
    metric_card,
    format_currency,
    download_dataframe,
    no_data
)

from charts import (
    loyalty_distribution,
    gender_distribution,
    age_distribution
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Customer Analytics",
    page_icon="👥",
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)

# ==========================================================
# LOAD DATA
# ==========================================================

with st.spinner("Loading customer analytics..."):
    df = load_data()

filtered_df = dashboard_sidebar(df)

if filtered_df.empty:
    no_data()

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
"""
<div class="hero">

<h1>
👥 Customer Analytics
</h1>

<p>

Understand customer behaviour,
loyalty and purchasing trends.

</p>

</div>
""",
unsafe_allow_html=True
)

st.caption(
    f"Last Updated : {last_refresh()}"
)

download_dataframe(
    filtered_df,
    "customer_dashboard.csv"
)

st.divider()

# ==========================================================
# KPIs
# ==========================================================

total_customers = filtered_df["CustomerID"].nunique()

avg_age = filtered_df["Age"].mean()

avg_customer_revenue = (

    filtered_df

    .groupby("CustomerID")["SalesAmount"]

    .sum()

    .mean()
)

avg_orders = (

    filtered_df

    .groupby("CustomerID")["SaleID"]

    .count()

    .mean()
)

c1, c2, c3, c4 = st.columns(4)

metric_card(
    c1,
    "👥 Customers",
    f"{total_customers:,}"
)

metric_card(
    c2,
    "🎂 Average Age",
    f"{avg_age:.1f}"
)

metric_card(
    c3,
    "💰 Avg Revenue",
    format_currency(avg_customer_revenue)
)

metric_card(
    c4,
    "🛒 Avg Orders",
    f"{avg_orders:.2f}"
)

st.divider()

# ==========================================================
# CUSTOMER SUMMARY
# ==========================================================

left, right = st.columns([2,1])

with left:

    st.subheader("📌 Customer Insights")

    st.markdown(f"""

- Total Customers: **{total_customers:,}**

- Average Age: **{avg_age:.1f} years**

- Average Customer Revenue:
**{format_currency(avg_customer_revenue)}**

- Average Orders per Customer:
**{avg_orders:.2f}**

""")

with right:

    st.info(f"""

Current Dataset

Rows

{len(filtered_df):,}

Cities

{filtered_df['City'].nunique()}

States

{filtered_df['State'].nunique()}

Loyalty Tiers

{filtered_df['LoyaltyTier'].nunique()}

""")

st.divider()

# ==========================================================
# ROW 1
# ==========================================================

left, right = st.columns(2)

# ----------------------------------------------------------
# Loyalty Distribution
# ----------------------------------------------------------

with left:

    st.plotly_chart(
        loyalty_distribution(filtered_df),
        use_container_width=True
    )

# ----------------------------------------------------------
# Gender Distribution
# ----------------------------------------------------------

with right:

    st.plotly_chart(
        gender_distribution(filtered_df),
        use_container_width=True
    )

st.divider()

# ==========================================================
# ROW 2
# ==========================================================

left, right = st.columns(2)

# ----------------------------------------------------------
# Age Distribution
# ----------------------------------------------------------

with left:

    st.plotly_chart(
        age_distribution(filtered_df),
        use_container_width=True
    )

# ----------------------------------------------------------
# Revenue by State
# ----------------------------------------------------------

with right:

    state_sales = (
        filtered_df
        .groupby("State", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
    )

    import plotly.express as px

    fig = px.bar(
        state_sales,
        x="State",
        y="SalesAmount",
        color="SalesAmount",
        title="🌍 Revenue by State",
        text_auto=".2s",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="Revenue"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# TOP CUSTOMERS
# ==========================================================

top_customers = (

    filtered_df

    .groupby(
        [
            "CustomerName",
            "City"
        ],
        as_index=False
    )["SalesAmount"]

    .sum()

    .sort_values(
        "SalesAmount",
        ascending=False
    )

    .head(10)
)

import plotly.express as px

fig = px.bar(

    top_customers,

    x="SalesAmount",

    y="CustomerName",

    orientation="h",

    color="SalesAmount",

    text_auto=".2s",

    title="🏆 Top 10 Customers by Revenue",

    color_continuous_scale="Viridis"
)

fig.update_layout(

    yaxis=dict(
        categoryorder="total ascending"
    ),

    xaxis_title="Revenue",

    yaxis_title=""
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# CUSTOMER LIFETIME VALUE
# ==========================================================

st.subheader("⭐ Customer Lifetime Value")

customer_summary = (

    filtered_df

    .groupby(
        [
            "CustomerID",
            "CustomerName",
            "City",
            "State",
            "LoyaltyTier"
        ],
        as_index=False
    )

    .agg(

        Orders=("SaleID","count"),

        Revenue=("SalesAmount","sum"),

        Profit=("ProfitAmount","sum"),

        Quantity=("Quantity","sum")
    )

    .sort_values(
        "Revenue",
        ascending=False
    )
)

customer_summary["Average Order Value"] = (

    customer_summary["Revenue"]

    /

    customer_summary["Orders"]
)

customer_summary["Profit Margin %"] = (

    customer_summary["Profit"]

    /

    customer_summary["Revenue"]

    *100
).round(2)

st.dataframe(

    customer_summary,

    use_container_width=True,

    hide_index=True
)

st.divider()

# ==========================================================
# LOYALTY INSIGHTS
# ==========================================================

st.subheader("🏅 Loyalty Insights")

loyalty = (

    filtered_df

    .groupby(
        "LoyaltyTier",
        as_index=False
    )

    .agg(

        Customers=("CustomerID","nunique"),

        Revenue=("SalesAmount","sum"),

        Profit=("ProfitAmount","sum")
    )
)

left,right=st.columns(2)

with left:

    st.dataframe(

        loyalty,

        use_container_width=True,

        hide_index=True
    )

with right:

    highest = loyalty.sort_values(
        "Revenue",
        ascending=False
    ).iloc[0]

    st.success(f"""

Highest Revenue Tier

🏆 {highest['LoyaltyTier']}

Revenue

₹ {highest['Revenue']:,.0f}

Profit

₹ {highest['Profit']:,.0f}

""")
    
st.divider()

# ==========================================================
# CUSTOMER STATISTICS
# ==========================================================

st.subheader("📈 Customer Statistics")

left,right=st.columns(2)

with left:

    st.metric(
        "Average Revenue",
        format_currency(
            customer_summary["Revenue"].mean()
        )
    )

    st.metric(
        "Highest Revenue",
        format_currency(
            customer_summary["Revenue"].max()
        )
    )

with right:

    st.metric(
        "Average Profit",
        format_currency(
            customer_summary["Profit"].mean()
        )
    )

    st.metric(
        "Highest Profit",
        format_currency(
            customer_summary["Profit"].max()
        )
    )

st.divider()

# ==========================================================
# DATA PREVIEW
# ==========================================================

with st.expander("🔍 View Customer Dataset"):

    st.dataframe(

        filtered_df,

        use_container_width=True,

        hide_index=True
    )


st.divider()

st.markdown(
"""
<div class="footer">

Retail Sales Analytics Platform

Customer Analytics Dashboard

Built with Python • MySQL • Streamlit • Plotly

</div>
""",
unsafe_allow_html=True
)

