"""
==========================================================
Retail Sales Data Warehouse
Business Constants
==========================================================
"""

# ==========================================================
# Customer
# ==========================================================

LOYALTY_TIERS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

GENDERS = [
    "Male",
    "Female",
    "Other"
]

# ==========================================================
# Payment Methods
# ==========================================================

PAYMENT_METHODS = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Wallet"
]

# ==========================================================
# Store
# ==========================================================

STORE_TYPES = [
    "Mall",
    "Standalone",
    "Supermarket",
    "Outlet"
]

STORE_SIZES = [
    "Small",
    "Medium",
    "Large"
]

REGIONS = [
    "North",
    "South",
    "East",
    "West"
]

# ==========================================================
# Product Categories
# ==========================================================

PRODUCT_CATEGORIES = {

    "Electronics": [
        "Smartphones",
        "Laptops",
        "Televisions",
        "Headphones",
        "Smart Watches"
    ],

    "Fashion": [
        "Men Clothing",
        "Women Clothing",
        "Footwear",
        "Accessories"
    ],

    "Home & Kitchen": [
        "Furniture",
        "Cookware",
        "Kitchen Appliances",
        "Home Decor"
    ],

    "Grocery": [
        "Beverages",
        "Snacks",
        "Dairy",
        "Bakery",
        "Fruits"
    ],

    "Beauty": [
        "Skincare",
        "Haircare",
        "Makeup",
        "Perfume"
    ],

    "Sports": [
        "Fitness",
        "Cricket",
        "Football",
        "Cycling"
    ]
}

# ==========================================================
# Brands
# ==========================================================

CATEGORY_BRANDS = {
    "Electronics": [
        "Apple",
        "Samsung",
        "Sony",
        "LG",
        "Dell",
        "HP",
        "Lenovo",
        "Boat"
    ],

    "Fashion": [
        "Nike",
        "Adidas",
        "Puma",
        "Levi's"
    ],

    "Grocery": [
        "Amul",
        "Nestle",
        "Britannia",
        "Tata"
    ],

    "Beauty": [
        "Lakme",
        "L'Oréal",
        "Maybelline"
    ],

    "Home & Kitchen": [
        "Prestige",
        "Milton",
        "Cello",
        "Godrej"
    ],

    "Sports": [
        "Nike",
        "Adidas",
        "Puma",
        "Yonex"
    ]
}

# ==========================================================
# Suppliers
# ==========================================================

SUPPLIERS = [
    "ABC Distributors",
    "Global Traders",
    "Prime Wholesale",
    "National Supply Co.",
    "Retail Source Pvt Ltd",
    "Star Distribution",
    "Sunrise Suppliers",
    "NextGen Imports",
    "Elite Wholesale",
    "Infinity Supply Chain"
]

# ==========================================================
# Indian States
# ==========================================================

STATES = [
    "Maharashtra",
    "Karnataka",
    "Tamil Nadu",
    "Kerala",
    "Telangana",
    "Gujarat",
    "Rajasthan",
    "Delhi",
    "Punjab",
    "West Bengal"
]

# ==========================================================
# Major Indian Cities
# ==========================================================

CITIES = {
    "Maharashtra": [
        "Mumbai",
        "Pune",
        "Nagpur"
    ],

    "Karnataka": [
        "Bengaluru",
        "Mysuru",
        "Mangaluru"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Coimbatore",
        "Madurai"
    ],

    "Kerala": [
        "Kochi",
        "Thiruvananthapuram",
        "Kozhikode"
    ],

    "Telangana": [
        "Hyderabad",
        "Warangal"
    ],

    "Gujarat": [
        "Ahmedabad",
        "Surat",
        "Vadodara"
    ],

    "Rajasthan": [
        "Jaipur",
        "Jodhpur",
        "Udaipur"
    ],

    "Delhi": [
        "New Delhi"
    ],

    "Punjab": [
        "Ludhiana",
        "Amritsar"
    ],

    "West Bengal": [
        "Kolkata",
        "Siliguri"
    ]
}

COUNTRY = "India"

STATE_REGION = {
    "Maharashtra": "West",
    "Gujarat": "West",

    "Karnataka": "South",
    "Kerala": "South",
    "Tamil Nadu": "South",
    "Telangana": "South",

    "Delhi": "North",
    "Punjab": "North",
    "Rajasthan": "North",

    "West Bengal": "East"
}