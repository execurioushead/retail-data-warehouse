"""
==========================================================
Retail Sales Data Warehouse
Configuration File
==========================================================
"""

from pathlib import Path

# ==========================================================
# Project Directories
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"

PROCESSED_DIR = DATA_DIR / "processed"

EXPORT_DIR = DATA_DIR / "exports"

# ==========================================================
# CSV File Paths
# ==========================================================

CUSTOMERS_FILE = RAW_DIR / "customers.csv"

PRODUCTS_FILE = RAW_DIR / "products.csv"

STORES_FILE = RAW_DIR / "stores.csv"

DATES_FILE = RAW_DIR / "dates.csv"

SALES_FILE = RAW_DIR / "sales.csv"

# ==========================================================
# Database Configuration
# ==========================================================

DB_HOST = "localhost"

DB_PORT = 3306

DB_NAME = "RetailDW"

DB_USER = "root"

# Homebrew MySQL on your Mac currently has no password
DB_PASSWORD = ""

# ==========================================================
# Data Generation Configuration
# ==========================================================

NUM_CUSTOMERS = 10_000

NUM_PRODUCTS = 2_000

NUM_STORES = 50

NUM_SALES = 100_000

START_DATE = "2018-01-01"

END_DATE = "2030-12-31"

# ==========================================================
# Random Seed
# ==========================================================

RANDOM_SEED = 42