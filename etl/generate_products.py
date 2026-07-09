"""
==========================================================
Retail Sales Data Warehouse
Generate Product Dimension
==========================================================
"""

import random

import pandas as pd
from tqdm import tqdm

from config import (
    PRODUCTS_FILE,
    NUM_PRODUCTS,
    RANDOM_SEED
)

from constants import (
    PRODUCT_CATEGORIES,
    CATEGORY_BRANDS,
    SUPPLIERS
)

from utils import (
    generate_product_code,
    random_boolean
)

random.seed(RANDOM_SEED)

products = []

print(f"\nGenerating {NUM_PRODUCTS:,} products...\n")

for product_id in tqdm(range(1, NUM_PRODUCTS + 1)):

    category = random.choice(list(PRODUCT_CATEGORIES.keys()))

    subcategory = random.choice(
        PRODUCT_CATEGORIES[category]
    )

    brand = random.choice(
        CATEGORY_BRANDS[category]
    )

    supplier = random.choice(SUPPLIERS)

    product_name = f"{brand} {subcategory}"

    cost_price = round(
        random.uniform(100, 50000),
        2
    )

    markup = random.uniform(1.10, 1.60)

    selling_price = round(
        cost_price * markup,
        2
    )

    products.append({

        "ProductID": product_id,

        "ProductCode": generate_product_code(product_id),

        "ProductName": product_name,

        "Category": category,

        "SubCategory": subcategory,

        "Brand": brand,

        "Supplier": supplier,

        "CostPrice": cost_price,

        "SellingPrice": selling_price,

        "IsActive": random_boolean()

    })

df = pd.DataFrame(products)

PRODUCTS_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    PRODUCTS_FILE,
    index=False
)

print("\nProducts generated successfully.")

print(df.head())