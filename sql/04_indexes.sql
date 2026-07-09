-- Indexes will be created here.
/*
==========================================================
Retail Sales Data Warehouse
File: 04_indexes.sql

Description:
Performance Optimization using Indexes
==========================================================
*/

USE RetailDW;

-- Customer
CREATE INDEX idx_sales_customer
ON FactSales(CustomerID);

-- Product
CREATE INDEX idx_sales_product
ON FactSales(ProductID);

-- Store
CREATE INDEX idx_sales_store
ON FactSales(StoreID);

-- Date
CREATE INDEX idx_sales_date
ON FactSales(DateID);

-- Composite
CREATE INDEX idx_sales_date_store
ON FactSales(DateID, StoreID);

CREATE INDEX idx_sales_product_date
ON FactSales(ProductID, DateID);