"""
==========================================================
Retail Sales Data Warehouse
Generate Date Dimension
==========================================================
"""

from datetime import datetime

import pandas as pd

from config import (
    DATES_FILE,
    START_DATE,
    END_DATE
)

print("\nGenerating Date Dimension...\n")

# ----------------------------------------------------------
# Generate Date Range
# ----------------------------------------------------------

dates = pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

records = []

for date in dates:

    records.append({

        "DateID": int(date.strftime("%Y%m%d")),

        "FullDate": date.date(),

        "DayNumber": date.day,

        "MonthNumber": date.month,

        "MonthName": date.strftime("%B"),

        "QuarterNumber": date.quarter,

        "YearNumber": date.year,

        "WeekdayName": date.strftime("%A"),

        "IsWeekend": date.weekday() >= 5

    })

df = pd.DataFrame(records)

DATES_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    DATES_FILE,
    index=False
)

print("Date Dimension generated successfully.\n")

print(df.head())

print(f"\nTotal Dates: {len(df):,}")