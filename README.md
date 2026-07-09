# 🏪 Retail Sales Data Warehouse

An end-to-end **Retail Sales Data Warehouse** built using **MySQL**, **Python**, and **Power BI**. This project demonstrates database design, ETL development, SQL analytics, query optimization, and business intelligence reporting using a star schema architecture.

---

## 📌 Project Overview

This project simulates a real-world retail data warehouse capable of storing and analyzing large volumes of retail sales data.

It includes:

- ⭐ Star Schema Data Warehouse
- 🔄 Python ETL Pipeline
- 📊 70+ Business Analytics SQL Queries
- ⚡ Query Optimization using Indexes
- 📑 SQL Views & Stored Procedures
- 📈 Power BI Dashboard (Coming Soon)

---

# 🏗️ Architecture

```
                Python ETL
                     │
                     ▼
          CSV Data Generation
                     │
                     ▼
              MySQL RetailDW
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
  Fact Table    Dimension Tables    Views
                     │
                     ▼
              Business Analytics
                     │
                     ▼
              Power BI Dashboard
```

---

# ⭐ Features

### Database Design

- Star Schema
- Fact Table
- 4 Dimension Tables
- Foreign Keys
- Business Keys
- Data Validation Constraints

### ETL Pipeline

- Customer Data Generator
- Product Data Generator
- Store Data Generator
- Date Generator
- Sales Generator
- Batch Loading into MySQL

### Performance Optimization

- Single Column Indexes
- Composite Indexes
- EXPLAIN Query Plans
- Optimized SQL Queries

### SQL Development

- Views
- Stored Procedures
- Window Functions
- Running Totals
- Moving Averages
- Customer Segmentation
- Time Intelligence
- Executive Business Insights

### Business Intelligence

- Executive KPIs
- Customer Analytics
- Product Analytics
- Store Analytics
- Payment Analytics
- Time Intelligence
- Revenue Analysis
- Profit Analysis

---

# 🗂️ Project Structure

```
retail-data-warehouse
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── docs/
│
├── etl/
│   ├── config.py
│   ├── constants.py
│   ├── generate_customers.py
│   ├── generate_products.py
│   ├── generate_stores.py
│   ├── generate_dates.py
│   ├── generate_sales.py
│   ├── load_mysql.py
│   └── utils.py
│
├── sql/
│   ├── 01_database.sql
│   ├── 02_dimensions.sql
│   ├── 03_fact_table.sql
│   ├── 04_indexes.sql
│   ├── 05_views.sql
│   ├── 06_procedures.sql
│   ├── 07_analytics.sql
│   └── 08_sales_analytics_view.sql
│
├── dashboard/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

---

# 🗄️ Data Warehouse Schema

## Dimension Tables

- DimCustomer
- DimProduct
- DimStore
- DimDate

## Fact Table

- FactSales

The warehouse follows a **Star Schema** optimized for analytical workloads.

---

# 📊 Analytics Modules

The project contains **70+ analytical SQL queries** covering:

- Executive KPIs
- Customer Analytics
- Product Analytics
- Store Analytics
- Time Intelligence
- Payment Analytics
- Window Functions
- Running Totals
- Customer Segmentation
- Executive Business Insights

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| MySQL | Data Warehouse |
| Python | ETL Pipeline |
| Pandas | Data Processing |
| Faker | Data Generation |
| MySQL Connector | Database Loading |
| Power BI | Dashboard & Reporting |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/retail-data-warehouse.git

cd retail-data-warehouse
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Database

```bash
mysql -u root < sql/01_database.sql
mysql -u root < sql/02_dimensions.sql
mysql -u root < sql/03_fact_table.sql
mysql -u root < sql/04_indexes.sql
mysql -u root < sql/05_views.sql
mysql -u root < sql/06_procedures.sql
mysql -u root < sql/07_analytics.sql
mysql -u root < sql/08_sales_analytics_view.sql
```

---

## Generate Data

```bash
python etl/generate_customers.py
python etl/generate_products.py
python etl/generate_stores.py
python etl/generate_dates.py
python etl/generate_sales.py
```

---

## Load Data

```bash
python etl/load_mysql.py
```

---

# 📈 Sample Business Questions Answered

- Which products generate the highest revenue?
- Which stores are most profitable?
- Which customer loyalty tier contributes the most revenue?
- What are the monthly sales trends?
- Which payment methods are most popular?
- Which regions drive the highest sales?
- Who are the top 20% of customers?
- What are the best-performing product categories?

---

# 📊 Power BI Dashboard

The dashboard includes:

- Executive Dashboard
- Customer Analytics
- Product Analytics
- Store Analytics
- Time Intelligence
- Payment Analytics

> Dashboard screenshots and `.pbix` file will be added soon.

---

# 📸 Screenshots

```
Coming Soon
```

---

# 🔮 Future Improvements

- Real-world retail dataset integration
- Incremental ETL pipeline
- Scheduled ETL automation
- Sales forecasting
- Customer churn prediction
- Docker support
- Cloud deployment (Azure/AWS)

---

# 👨‍💻 Author

**Rayan Prabhu**

GitHub: https://github.com/execurioushead



---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project helpful, consider giving it a star!