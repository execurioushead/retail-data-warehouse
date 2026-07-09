"""
==========================================================
Retail Sales Analytics Platform
Utility Functions
==========================================================
"""

import streamlit as st
import pandas as pd

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

def dashboard_sidebar(df: pd.DataFrame):

    st.sidebar.title("📊 Dashboard Filters")

    # ------------------------
    # Year
    # ------------------------

    years = sorted(df["YearNumber"].unique())

    selected_year = st.sidebar.selectbox(
        "📅 Year",
        years,
        index=len(years)-1
    )

    # ------------------------
    # Region
    # ------------------------

    regions = sorted(df["Region"].unique())

    selected_regions = st.sidebar.multiselect(
        "🌍 Region",
        regions,
        default=regions
    )

    # ------------------------
    # Category
    # ------------------------

    categories = sorted(df["Category"].unique())

    selected_categories = st.sidebar.multiselect(
        "📦 Category",
        categories,
        default=categories
    )

    # ------------------------
    # Store
    # ------------------------

    stores = sorted(df["StoreName"].unique())

    selected_stores = st.sidebar.multiselect(
        "🏬 Store",
        stores,
        default=stores
    )

    filtered = df[
        (df["YearNumber"] == selected_year)
        &
        (df["Region"].isin(selected_regions))
        &
        (df["Category"].isin(selected_categories))
        &
        (df["StoreName"].isin(selected_stores))
    ]

    st.sidebar.markdown("---")

    st.sidebar.caption(
        f"{len(filtered):,} records selected"
    )

    return filtered


# ==========================================================
# CURRENCY FORMATTER
# ==========================================================

def format_currency(value):

    if value >= 1_000_000_000:
        return f"₹ {value/1_000_000_000:.2f}B"

    if value >= 1_000_000:
        return f"₹ {value/1_000_000:.2f}M"

    if value >= 1_000:
        return f"₹ {value/1_000:.2f}K"

    return f"₹ {value:.0f}"


# ==========================================================
# NUMBER FORMATTER
# ==========================================================

def format_number(value):

    if value >= 1_000_000:
        return f"{value/1_000_000:.2f}M"

    if value >= 1_000:
        return f"{value/1_000:.2f}K"

    return f"{value}"


# ==========================================================
# KPI CARD
# ==========================================================

def metric_card(column, label, value):

    with column:

        st.metric(
            label=label,
            value=value
        )


# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

def download_dataframe(df, filename):

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download CSV",
        data=csv,
        file_name=filename,
        mime="text/csv",
        use_container_width=True
    )


# ==========================================================
# PAGE HEADER
# ==========================================================

def page_header(title, subtitle):

    st.markdown(
        f"""
# {title}

{subtitle}
""")
    
    
# ==========================================================
# EMPTY DATA MESSAGE
# ==========================================================

def no_data():

    st.warning(
        "No data available for the selected filters."
    )

    st.stop()