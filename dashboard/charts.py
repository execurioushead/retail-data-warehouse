"""
==========================================================
Retail Sales Analytics Platform
Reusable Plotly Charts
==========================================================
"""

import plotly.express as px

from config import (
    PRIMARY,
    SECONDARY,
    SUCCESS,
    WARNING,
    DANGER,
    PLOTLY_TEMPLATE,
    PLOT_HEIGHT
)

# ==========================================================
# COMMON LAYOUT
# ==========================================================

def apply_layout(fig):

    fig.update_layout(

        template=PLOTLY_TEMPLATE,

        height=PLOT_HEIGHT,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        title_x=.02,

        font=dict(
            family="Inter",
            size=14
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend_title=None
    )

    return fig


# ==========================================================
# MONTHLY REVENUE
# ==========================================================

def monthly_revenue(df):

    monthly = (

        df

        .groupby(
            ["MonthNumber","MonthName"],
            as_index=False
        )["SalesAmount"]

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

    fig.update_traces(

        line=dict(width=4),

        marker=dict(size=8)
    )

    return apply_layout(fig)


# ==========================================================
# CATEGORY REVENUE
# ==========================================================

def revenue_by_category(df):

    category = (

        df

        .groupby(
            "Category",
            as_index=False
        )["SalesAmount"]

        .sum()

        .sort_values(
            "SalesAmount",
            ascending=False
        )
    )

    fig = px.bar(

        category,

        x="Category",

        y="SalesAmount",

        color="Category",

        title="📦 Revenue by Category"
    )

    return apply_layout(fig)


# ==========================================================
# REGION REVENUE
# ==========================================================

def revenue_by_region(df):

    region = (

        df

        .groupby(
            "Region",
            as_index=False
        )["SalesAmount"]

        .sum()
    )

    fig = px.bar(

        region,

        x="Region",

        y="SalesAmount",

        color="Region",

        title="🌍 Revenue by Region"
    )

    return apply_layout(fig)


# ==========================================================
# PAYMENT DISTRIBUTION
# ==========================================================

def payment_distribution(df):

    payment = (

        df

        .groupby(
            "PaymentMethod",
            as_index=False
        )["SalesAmount"]

        .sum()
    )

    fig = px.pie(

        payment,

        values="SalesAmount",

        names="PaymentMethod",

        hole=.60,

        title="💳 Payment Distribution"
    )

    return apply_layout(fig)


# ==========================================================
# TOP PRODUCTS
# ==========================================================

def top_products(df):

    products = (

        df

        .groupby(
            "ProductName",
            as_index=False
        )["SalesAmount"]

        .sum()

        .sort_values(
            "SalesAmount",
            ascending=False
        )

        .head(10)
    )

    fig = px.bar(

        products,

        x="SalesAmount",

        y="ProductName",

        orientation="h",

        title="🏆 Top Products"
    )

    fig.update_layout(

        yaxis=dict(
            categoryorder="total ascending"
        )
    )

    return apply_layout(fig)


# ==========================================================
# LOYALTY DISTRIBUTION
# ==========================================================

def loyalty_distribution(df):

    loyalty = (

        df

        .groupby(
            "LoyaltyTier",
            as_index=False
        )

        .size()

        .rename(
            columns={
                "size":"Customers"
            }
        )
    )

    fig = px.pie(

        loyalty,

        values="Customers",

        names="LoyaltyTier",

        hole=.55,

        title="🏅 Loyalty Distribution"
    )

    return apply_layout(fig)


# ==========================================================
# GENDER DISTRIBUTION
# ==========================================================

def gender_distribution(df):

    gender = (

        df

        .groupby(
            "Gender",
            as_index=False
        )

        .size()

        .rename(
            columns={
                "size":"Customers"
            }
        )
    )

    fig = px.bar(

        gender,

        x="Gender",

        y="Customers",

        color="Gender",

        title="👥 Gender Distribution"
    )

    return apply_layout(fig)


# ==========================================================
# AGE HISTOGRAM
# ==========================================================

def age_distribution(df):

    fig = px.histogram(

        df,

        x="Age",

        nbins=20,

        title="🎂 Age Distribution"
    )

    return apply_layout(fig)