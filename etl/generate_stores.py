"""
==========================================================
Retail Sales Data Warehouse
Generate Store Dimension
==========================================================
"""

import random

import pandas as pd
from tqdm import tqdm

from config import (
    STORES_FILE,
    NUM_STORES,
    RANDOM_SEED,
    START_DATE,
    END_DATE
)

from constants import (
    STORE_TYPES,
    STORE_SIZES,
    REGIONS,
    STATES,
    CITIES,
    COUNTRY
)

from utils import (
    generate_store_code,
    random_date
)

random.seed(RANDOM_SEED)

stores = []

print(f"\nGenerating {NUM_STORES:,} stores...\n")

for store_id in tqdm(range(1, NUM_STORES + 1)):

    state = random.choice(STATES)

    city = random.choice(CITIES[state])

    from constants import STATE_REGION

    region = STATE_REGION[state]

    store_type = random.choice(STORE_TYPES)

    store_size = random.choice(STORE_SIZES)

    store_name = f"{city} {store_type}"

    stores.append({

        "StoreID": store_id,

        "StoreCode": generate_store_code(store_id),

        "StoreName": store_name,

        "StoreType": store_type,

        "Region": region,

        "StoreSize": store_size,

        "City": city,

        "State": state,

        "Country": COUNTRY,

        "OpeningDate": random_date(
            START_DATE,
            END_DATE
        ).date()

    })

df = pd.DataFrame(stores)

STORES_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    STORES_FILE,
    index=False
)

print("\nStores generated successfully.\n")

print(df.head())