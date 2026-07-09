"""
==========================================================
Retail Sales Analytics Platform
Executive Dashboard
==========================================================
"""

import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT,
    SIDEBAR_STATE,
)

from db import (
    load_data,
    last_refresh,
)

from utils import (
    dashboard_sidebar,
    metric_card,
    format_currency,
    download_dataframe,
    no_data,
)

from charts import (
    monthly_revenue,
    revenue_by_category,
    revenue_by_region,
    payment_distribution,
    top_products,
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)

# ==========================================================
# LOAD DATA
# ==========================================================

with st.spinner("Loading dashboard..."):

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

<h1>📊 Executive Dashboard</h1>

<p>
Executive overview of sales, profitability,
customers and products.
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
    "executive_dashboard.csv"
)

st.divider()

# ==========================================================
# KPIs
# ==========================================================

total_revenue = filtered_df["SalesAmount"].sum()

total_profit = filtered_df["ProfitAmount"].sum()

total_orders = filtered_df["SaleID"].count()

total_customers = filtered_df["CustomerID"].nunique()

c1, c2, c3, c4 = st.columns(4)

metric_card(
    c1,
    "💰 Revenue",
    format_currency(total_revenue)
)

metric_card(
    c2,
    "📈 Profit",
    format_currency(total_profit)
)

metric_card(
    c3,
    "🛒 Orders",
    f"{total_orders:,}"
)

metric_card(
    c4,
    "👥 Customers",
    f"{total_customers:,}"
)

st.divider()

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

avg_order_value = (
    total_revenue / total_orders
    if total_orders
    else 0
)

profit_margin = (
    (total_profit / total_revenue) * 100
    if total_revenue
    else 0
)

left, right = st.columns([2, 1])

with left:

    st.subheader("📌 Executive Summary")

    st.markdown(f"""
- **Revenue:** {format_currency(total_revenue)}
- **Profit:** {format_currency(total_profit)}
- **Orders:** {total_orders:,}
- **Customers:** {total_customers:,}
- **Average Order Value:** {format_currency(avg_order_value)}
- **Profit Margin:** {profit_margin:.2f}%
""")

with right:

    st.info(
f"""
**Current Selection**

Records: {len(filtered_df):,}

Years: {filtered_df['YearNumber'].nunique()}

Regions: {filtered_df['Region'].nunique()}

Categories: {filtered_df['Category'].nunique()}
"""
    )

st.divider()

# ==========================================================
# ROW 1
# ==========================================================

left, right = st.columns(2)

with left:

    st.plotly_chart(
        monthly_revenue(filtered_df),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        revenue_by_category(filtered_df),
        use_container_width=True
    )

# ==========================================================
# ROW 2
# ==========================================================

left, right = st.columns(2)

with left:

    st.plotly_chart(
        revenue_by_region(filtered_df),
        use_container_width=True
    )

with right:

    st.plotly_chart(
        payment_distribution(filtered_df),
        use_container_width=True
    )

# ==========================================================
# TOP PRODUCTS
# ==========================================================

st.plotly_chart(
    top_products(filtered_df),
    use_container_width=True
)

st.divider()

# ==========================================================
# DATA PREVIEW
# ==========================================================

with st.expander("🔍 View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
    )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
<div class="footer">

Retail Sales Analytics Platform

Built using Python • MySQL • Streamlit • Plotly

</div>
""",
unsafe_allow_html=True
)