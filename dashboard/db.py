"""
==========================================================
Retail Sales Analytics Platform
Database Module
==========================================================
"""

import os
from datetime import datetime

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

# ==========================================================
# DATABASE CONFIGURATION
# ==========================================================

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "RetailDW")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==========================================================
# ENGINE
# ==========================================================

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=5,
    max_overflow=10,
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data(show_spinner=False)
def load_data():
    """
    Load the analytics view into a Pandas DataFrame.
    Cached by Streamlit for better performance.
    """
    query = """
    SELECT *
    FROM vw_SalesAnalytics;
    """

    try:
        return pd.read_sql(query, engine)

    except SQLAlchemyError as e:
        st.error(f"Database Error:\n{e}")
        return pd.DataFrame()

# ==========================================================
# EXECUTE QUERY
# ==========================================================

def run_query(query: str):
    """
    Execute any SELECT query and return a DataFrame.
    """
    try:
        return pd.read_sql(query, engine)

    except SQLAlchemyError as e:
        st.error(f"Query Error:\n{e}")
        return pd.DataFrame()

# ==========================================================
# LAST REFRESH
# ==========================================================

def last_refresh():
    """
    Return the current timestamp for dashboard display.
    """
    return datetime.now().strftime("%d %b %Y • %I:%M %p")