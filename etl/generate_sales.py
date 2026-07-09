"""
==========================================================
Retail Sales Data Warehouse
Generate Sales Fact Table
Part 1
==========================================================
"""

import random

import pandas as pd
from tqdm import tqdm

from config import (
    CUSTOMERS_FILE,
    PRODUCTS_FILE,
    STORES_FILE,
    DATES_FILE,
    SALES_FILE,
    NUM_SALES,
    RANDOM_SEED
)

from constants import PAYMENT_METHODS

from utils import (
    calculate_sales_amount,
    calculate_cost_amount,
    calculate_profit
)

# ==========================================================
# Random Seed
# ==========================================================

random.seed(RANDOM_SEED)

# ==========================================================
# Load Dimension Tables
# ==========================================================

print("\nLoading Dimension Tables...\n")

customers = pd.read_csv(CUSTOMERS_FILE)

products = pd.read_csv(PRODUCTS_FILE)

stores = pd.read_csv(STORES_FILE)

dates = pd.read_csv(DATES_FILE)

print(f"Customers : {len(customers):,}")

print(f"Products  : {len(products):,}")

print(f"Stores    : {len(stores):,}")

print(f"Dates     : {len(dates):,}")

# ==========================================================
# Prepare Lookup Lists
# ==========================================================

customer_ids = customers["CustomerID"].tolist()

product_ids = products["ProductID"].tolist()

store_ids = stores["StoreID"].tolist()

date_ids = dates["DateID"].tolist()

# ==========================================================
# Product Lookup Dictionary
# ==========================================================

product_lookup = (
    products
    .set_index("ProductID")
    .to_dict("index")
)

# ==========================================================
# Sales Container
# ==========================================================

sales = []

print("\nStarting Sales Generation...\n")

# ==========================================================
# Generate Sales Transactions
# ==========================================================

print(f"\nGenerating {NUM_SALES:,} sales records...\n")

for sale_id in tqdm(range(1, NUM_SALES + 1)):

    # ------------------------------------------------------
    # Random Dimension Keys
    # ------------------------------------------------------

    customer_id = random.choice(customer_ids)

    product_id = random.choice(product_ids)

    store_id = random.choice(store_ids)

    date_id = random.choice(date_ids)

    # ------------------------------------------------------
    # Product Information
    # ------------------------------------------------------

    product = product_lookup[product_id]

    cost_price = float(product["CostPrice"])

    selling_price = float(product["SellingPrice"])

    # ------------------------------------------------------
    # Transaction Details
    # ------------------------------------------------------

    quantity = random.randint(1, 5)

    unit_price = selling_price

    # Around 30% of orders receive a discount
    if random.random() < 0.30:

        discount = round(
            unit_price * quantity * random.uniform(0.05, 0.20),
            2
        )

    else:

        discount = 0.0

    # ------------------------------------------------------
    # Financial Calculations
    # ------------------------------------------------------

    sales_amount = calculate_sales_amount(
        quantity,
        unit_price,
        discount
    )

    cost_amount = calculate_cost_amount(
        quantity,
        cost_price
    )

    profit_amount = calculate_profit(
        sales_amount,
        cost_amount
    )

    # ------------------------------------------------------
    # Payment Method
    # ------------------------------------------------------

    payment_method = random.choices(

        population=PAYMENT_METHODS,

        weights=[15, 20, 15, 35, 5, 10],

        k=1

    )[0]

    # ------------------------------------------------------
    # Append Record
    # ------------------------------------------------------

    sales.append({

        "SaleID": sale_id,

        "CustomerID": customer_id,

        "ProductID": product_id,

        "StoreID": store_id,

        "DateID": date_id,

        "Quantity": quantity,

        "UnitPrice": unit_price,

        "DiscountAmount": discount,

        "SalesAmount": sales_amount,

        "CostAmount": cost_amount,

        "ProfitAmount": profit_amount,

        "PaymentMethod": payment_method

    })

print("\nSales generation completed.\n")

# ==========================================================
# Create DataFrame
# ==========================================================

df = pd.DataFrame(sales)

# ==========================================================
# Data Validation
# ==========================================================

print("\nRunning validation checks...\n")

assert len(df) == NUM_SALES, "Incorrect number of sales records."

assert df["Quantity"].min() > 0, "Invalid Quantity found."

assert df["UnitPrice"].min() > 0, "Invalid UnitPrice found."

assert df["DiscountAmount"].min() >= 0, "Negative Discount found."

assert df["SalesAmount"].min() >= 0, "Negative SalesAmount found."

assert df["CostAmount"].min() >= 0, "Negative CostAmount found."

assert df["CustomerID"].isin(customer_ids).all(), "Invalid CustomerID."

assert df["ProductID"].isin(product_ids).all(), "Invalid ProductID."

assert df["StoreID"].isin(store_ids).all(), "Invalid StoreID."

assert df["DateID"].isin(date_ids).all(), "Invalid DateID."

print("All validation checks passed.")

# ==========================================================
# Save CSV
# ==========================================================

SALES_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    SALES_FILE,
    index=False
)

print("\nSales CSV created successfully.")

print(f"\nLocation:\n{SALES_FILE}")

print("\nPreview:\n")

print(df.head())

print(f"\nTotal Sales Records : {len(df):,}")

print(f"Total Revenue       : ₹{df['SalesAmount'].sum():,.2f}")

print(f"Total Profit        : ₹{df['ProfitAmount'].sum():,.2f}")

