"""
==========================================================
Retail Sales Data Warehouse
Load CSV Files into MySQL
Part 1
==========================================================
"""

import mysql.connector
import pandas as pd

from config import (
    PROJECT_ROOT,
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    CUSTOMERS_FILE,
    PRODUCTS_FILE,
    STORES_FILE,
    DATES_FILE,
    SALES_FILE
)

# ==========================================================
# Connect to MySQL
# ==========================================================

print("\nConnecting to MySQL...\n")

connection = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    ssl_ca=str(PROJECT_ROOT / "ca.pem"),
    ssl_verify_cert=True
)

cursor = connection.cursor()

print("Connected successfully.")

# ==========================================================
# Load CSV Files
# ==========================================================

print("\nLoading CSV files...\n")

customers = pd.read_csv(CUSTOMERS_FILE)

products = pd.read_csv(PRODUCTS_FILE)

stores = pd.read_csv(STORES_FILE)

dates = pd.read_csv(DATES_FILE)

sales = pd.read_csv(SALES_FILE)

print(f"Customers : {len(customers):,}")

print(f"Products  : {len(products):,}")

print(f"Stores    : {len(stores):,}")

print(f"Dates     : {len(dates):,}")

print(f"Sales     : {len(sales):,}")

print("\nCSV files loaded successfully.\n")

# ==========================================================
# Helper Function
# ==========================================================

def insert_dataframe(table_name, dataframe):
    """
    Insert a pandas DataFrame into a MySQL table.
    """

    print(f"\nLoading {table_name}...")

    columns = ", ".join(dataframe.columns)

    placeholders = ", ".join(["%s"] * len(dataframe.columns))

    sql = f"""
        INSERT INTO {table_name}
        ({columns})
        VALUES ({placeholders})
    """

    data = dataframe.values.tolist()

    cursor.executemany(sql, data)

    connection.commit()

    print(f"{cursor.rowcount:,} rows inserted into {table_name}.")


# ==========================================================
# Clear Existing Data
# ==========================================================

print("\nClearing existing data...\n")

cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

cursor.execute("TRUNCATE TABLE FactSales;")
cursor.execute("TRUNCATE TABLE DimCustomer;")
cursor.execute("TRUNCATE TABLE DimProduct;")
cursor.execute("TRUNCATE TABLE DimStore;")
cursor.execute("TRUNCATE TABLE DimDate;")

cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

connection.commit()

print("Old data removed successfully.\n")


# ==========================================================
# Load Dimension Tables
# ==========================================================

insert_dataframe(
    "DimCustomer",
    customers
)

insert_dataframe(
    "DimProduct",
    products
)

insert_dataframe(
    "DimStore",
    stores
)

insert_dataframe(
    "DimDate",
    dates
)

print("\nAll Dimension Tables Loaded Successfully.\n")

# ==========================================================
# Load FactSales in Batches
# ==========================================================

print("\nLoading FactSales...\n")

BATCH_SIZE = 5000

columns = ", ".join(sales.columns)

placeholders = ", ".join(["%s"] * len(sales.columns))

sql = f"""
INSERT INTO FactSales
({columns})
VALUES ({placeholders})
"""

total_rows = len(sales)

for start in range(0, total_rows, BATCH_SIZE):

    end = min(start + BATCH_SIZE, total_rows)

    batch = sales.iloc[start:end]

    cursor.executemany(
        sql,
        batch.values.tolist()
    )

    connection.commit()

    print(f"Loaded rows {start+1:,} - {end:,}")

print("\nFactSales loaded successfully.")

# ==========================================================
# Validation
# ==========================================================

print("\nValidating row counts...\n")

tables = [
    "DimCustomer",
    "DimProduct",
    "DimStore",
    "DimDate",
    "FactSales"
]

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"{table:<15}: {count:,} rows")

# ==========================================================
# Close Connection
# ==========================================================

cursor.close()

connection.close()

print("\nMySQL connection closed.")

print("\n===================================")
print("RetailDW ETL Completed Successfully")
print("===================================")