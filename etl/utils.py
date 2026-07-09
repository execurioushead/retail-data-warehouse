"""
==========================================================
Retail Sales Data Warehouse
Utility Functions
==========================================================
"""

import random
from datetime import datetime, timedelta

from faker import Faker

from config import RANDOM_SEED

# ==========================================================
# Faker Initialization
# ==========================================================

fake = Faker("en_IN")

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)

# ==========================================================
# Business Key Generators
# ==========================================================

def generate_customer_code(customer_id: int) -> str:
    """
    Generate customer business key.
    Example:
        CUST000001
    """
    return f"CUST{customer_id:06d}"


def generate_product_code(product_id: int) -> str:
    """
    Generate product business key.
    Example:
        PROD000001
    """
    return f"PROD{product_id:06d}"


def generate_store_code(store_id: int) -> str:
    """
    Generate store business key.
    Example:
        STORE001
    """
    return f"STORE{store_id:03d}"


# ==========================================================
# Customer Helpers
# ==========================================================

def generate_email(first_name: str, last_name: str) -> str:
    """
    Generate a realistic email address.
    """
    domains = [
        "gmail.com",
        "outlook.com",
        "yahoo.com",
        "icloud.com"
    ]

    return (
        f"{first_name.lower()}."
        f"{last_name.lower()}"
        f"{random.randint(100,999)}@"
        f"{random.choice(domains)}"
    )


# ==========================================================
# Date Helpers
# ==========================================================

def random_date(start_date: str, end_date: str):
    """
    Return a random date between two dates.
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    delta = end - start

    random_days = random.randint(0, delta.days)

    return start + timedelta(days=random_days)


# ==========================================================
# Pricing Helpers
# ==========================================================

def calculate_sales_amount(
    quantity: int,
    unit_price: float,
    discount: float
) -> float:
    """
    Calculate total sales amount.
    """

    return round(quantity * unit_price - discount, 2)


def calculate_cost_amount(
    quantity: int,
    cost_price: float
) -> float:
    """
    Calculate total cost.
    """

    return round(quantity * cost_price, 2)


def calculate_profit(
    sales_amount: float,
    cost_amount: float
) -> float:
    """
    Calculate profit.
    """

    return round(sales_amount - cost_amount, 2)


# ==========================================================
# Misc Helpers
# ==========================================================

def random_boolean(true_probability=0.9):
    """
    Returns True most of the time.
    Useful for IsActive.
    """

    return random.random() < true_probability