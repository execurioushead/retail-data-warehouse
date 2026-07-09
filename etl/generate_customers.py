"""
==========================================================
Retail Sales Data Warehouse
Generate Customer Dimension
==========================================================
"""

import random

import pandas as pd
from tqdm import tqdm

from faker import Faker

from config import (
    CUSTOMERS_FILE,
    NUM_CUSTOMERS,
    START_DATE,
    END_DATE,
    RANDOM_SEED
)

from constants import (
    GENDERS,
    LOYALTY_TIERS,
    STATES,
    CITIES,
    COUNTRY
)

from utils import (
    generate_customer_code,
    generate_email,
    random_date
)

# ==========================================================
# Faker Setup
# ==========================================================

fake = Faker("en_IN")

random.seed(RANDOM_SEED)
Faker.seed(RANDOM_SEED)

# ==========================================================
# Generate Customers
# ==========================================================

customers = []

print(f"\nGenerating {NUM_CUSTOMERS:,} customers...\n")

for customer_id in tqdm(range(1, NUM_CUSTOMERS + 1)):

    gender = random.choice(GENDERS)

    if gender == "Male":
        first_name = fake.first_name_male()
    elif gender == "Female":
        first_name = fake.first_name_female()
    else:
        first_name = fake.first_name()

    last_name = fake.last_name()

    state = random.choice(STATES)

    city = random.choice(CITIES[state])

    customer = {

        "CustomerID": customer_id,

        "CustomerCode": generate_customer_code(customer_id),

        "FirstName": first_name,

        "LastName": last_name,

        "Gender": gender,

        "Age": random.randint(18, 80),

        "Email": generate_email(
            first_name,
            last_name
        ),

        "City": city,

        "State": state,

        "Country": COUNTRY,

        "LoyaltyTier": random.choices(
            population=LOYALTY_TIERS,
            weights=[50, 30, 15, 5],
            k=1
        )[0],

        "JoinDate": random_date(
            START_DATE,
            END_DATE
        ).date()

    }

    customers.append(customer)

# ==========================================================
# Create DataFrame
# ==========================================================

df = pd.DataFrame(customers)

# ==========================================================
# Save CSV
# ==========================================================

CUSTOMERS_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    CUSTOMERS_FILE,
    index=False
)

print("\nCustomer generation completed.")

print(f"\nCSV saved to:\n{CUSTOMERS_FILE}")

print("\nPreview:\n")

print(df.head())