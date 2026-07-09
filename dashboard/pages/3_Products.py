"""
==========================================================
Retail Sales Analytics Platform
Product Analytics Dashboard
==========================================================
"""

import streamlit as st
import plotly.express as px

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

st.set_page_config(
    page_title="Product Analytics",
    page_icon="📦",
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)

# ==========================================================
# LOAD DATA
# ==========================================================

with st.spinner("Loading Product Analytics..."):
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

<h1>📦 Product Analytics</h1>

<p>

Analyze products, categories, suppliers,
brands and profitability.

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
    "product_dashboard.csv"
)

st.divider()

# ==========================================================
# KPIs
# ==========================================================

total_products = filtered_df["ProductID"].nunique()

total_categories = filtered_df["Category"].nunique()

total_brands = filtered_df["Brand"].nunique()

avg_product_revenue = (

    filtered_df

    .groupby("ProductID")["SalesAmount"]

    .sum()

    .mean()
)

c1, c2, c3, c4 = st.columns(4)

metric_card(
    c1,
    "📦 Products",
    f"{total_products:,}"
)

metric_card(
    c2,
    "🏷 Categories",
    total_categories
)

metric_card(
    c3,
    "🏢 Brands",
    total_brands
)

metric_card(
    c4,
    "💰 Avg Revenue",
    format_currency(avg_product_revenue)
)

st.divider()

# ==========================================================
# PRODUCT SUMMARY
# ==========================================================

left, right = st.columns([2,1])

with left:

    st.subheader("📌 Product Insights")

    st.markdown(f"""

- Products: **{total_products:,}**

- Categories: **{total_categories}**

- Brands: **{total_brands}**

- Average Product Revenue:
**{format_currency(avg_product_revenue)}**

""")

with right:

    st.info(f"""

Dataset Summary

Rows

{len(filtered_df):,}

Suppliers

{filtered_df['Supplier'].nunique()}

Categories

{filtered_df['Category'].nunique()}

Brands

{filtered_df['Brand'].nunique()}

""")

st.divider()

# ==========================================================
# ROW 1
# ==========================================================

left, right = st.columns(2)

# ----------------------------------------------------------
# Revenue by Category
# ----------------------------------------------------------

with left:

    category_sales = (
        filtered_df
        .groupby("Category", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
    )

    fig = px.bar(
        category_sales,
        x="Category",
        y="SalesAmount",
        color="SalesAmount",
        title="📦 Revenue by Category",
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

# ----------------------------------------------------------
# Revenue by Brand
# ----------------------------------------------------------

with right:

    brand_sales = (
        filtered_df
        .groupby("Brand", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
    )

    fig = px.bar(
        brand_sales,
        x="Brand",
        y="SalesAmount",
        color="SalesAmount",
        title="🏢 Revenue by Brand",
        text_auto=".2s",
        color_continuous_scale="Viridis"
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
# ROW 2
# ==========================================================

left, right = st.columns(2)

# ----------------------------------------------------------
# Top Suppliers
# ----------------------------------------------------------

with left:

    supplier_sales = (
        filtered_df
        .groupby("Supplier", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
        .head(10)
    )

    fig = px.bar(
        supplier_sales,
        x="SalesAmount",
        y="Supplier",
        orientation="h",
        color="SalesAmount",
        text_auto=".2s",
        title="🚚 Top Suppliers",
        color_continuous_scale="Turbo"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------------
# Top Products
# ----------------------------------------------------------

with right:

    top_products = (
        filtered_df
        .groupby("ProductName", as_index=False)["SalesAmount"]
        .sum()
        .sort_values("SalesAmount", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_products,
        x="SalesAmount",
        y="ProductName",
        orientation="h",
        color="SalesAmount",
        text_auto=".2s",
        title="🏆 Top Products",
        color_continuous_scale="Plasma"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# PRODUCT REVENUE DISTRIBUTION
# ==========================================================

fig = px.histogram(
    filtered_df,
    x="SalesAmount",
    nbins=40,
    title="📈 Product Revenue Distribution",
    color_discrete_sequence=["#3B82F6"]
)

fig.update_layout(
    xaxis_title="Revenue",
    yaxis_title="Frequency"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# PRODUCT PROFITABILITY
# ==========================================================

st.subheader("⭐ Product Profitability")

product_summary = (

    filtered_df

    .groupby(
        [
            "ProductID",
            "ProductName",
            "Category",
            "Brand",
            "Supplier"
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

product_summary["Average Selling Price"] = (

    product_summary["Revenue"]

    /

    product_summary["Quantity"]
).round(2)

product_summary["Profit Margin %"] = (

    product_summary["Profit"]

    /

    product_summary["Revenue"]

    *100
).round(2)

st.dataframe(
    product_summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# CATEGORY PERFORMANCE
# ==========================================================

st.subheader("📦 Category Performance")

category_summary = (

    filtered_df

    .groupby(
        "Category",
        as_index=False
    )

    .agg(

        Products=("ProductID","nunique"),

        Revenue=("SalesAmount","sum"),

        Profit=("ProfitAmount","sum"),

        Quantity=("Quantity","sum")
    )

    .sort_values(
        "Revenue",
        ascending=False
    )
)

left,right = st.columns(2)

with left:

    st.dataframe(

        category_summary,

        use_container_width=True,

        hide_index=True
    )

with right:

    best = category_summary.iloc[0]

    st.success(f"""

🏆 Best Performing Category

**{best['Category']}**

Revenue

₹ {best['Revenue']:,.0f}

Profit

₹ {best['Profit']:,.0f}

Products

{best['Products']}

""")
    

st.divider()

# ==========================================================
# PRODUCT STATISTICS
# ==========================================================

st.subheader("📈 Product Statistics")

left,right = st.columns(2)

with left:

    st.metric(

        "Average Product Revenue",

        format_currency(
            product_summary["Revenue"].mean()
        )
    )

    st.metric(

        "Highest Product Revenue",

        format_currency(
            product_summary["Revenue"].max()
        )
    )

with right:

    st.metric(

        "Average Product Profit",

        format_currency(
            product_summary["Profit"].mean()
        )
    )

    st.metric(

        "Highest Product Profit",

        format_currency(
            product_summary["Profit"].max()
        )
    )

st.divider()

# ==========================================================
# PRODUCT EXPLORER
# ==========================================================

st.subheader("🔍 Product Explorer")

search = st.text_input(
    "Search Product"
)

display_df = product_summary.copy()

if search:

    display_df = display_df[
        display_df["ProductName"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

st.dataframe(

    display_df,

    use_container_width=True,

    hide_index=True
)

st.divider()

st.markdown(
"""
<div class="footer">

Retail Sales Analytics Platform

Product Analytics Dashboard

Built using Python • MySQL • Streamlit • Plotly

</div>
""",
unsafe_allow_html=True
)

