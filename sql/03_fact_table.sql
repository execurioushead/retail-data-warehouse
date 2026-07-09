/*
==========================================================
Retail Sales Data Warehouse
File: 03_fact_table.sql
Description:
Creates the Sales Fact Table
==========================================================
*/

USE RetailDW;

DROP TABLE IF EXISTS FactSales;

CREATE TABLE FactSales (

    SaleID BIGINT AUTO_INCREMENT PRIMARY KEY,

    CustomerID INT NOT NULL,

    ProductID INT NOT NULL,

    StoreID INT NOT NULL,

    DateID INT NOT NULL,

    Quantity SMALLINT UNSIGNED NOT NULL,

    UnitPrice DECIMAL(10,2) NOT NULL,

    DiscountAmount DECIMAL(10,2) NOT NULL DEFAULT 0,

    SalesAmount DECIMAL(12,2) NOT NULL,

    CostAmount DECIMAL(12,2) NOT NULL,

    ProfitAmount DECIMAL(12,2) NOT NULL,

    PaymentMethod ENUM(
        'Cash',
        'Credit Card',
        'Debit Card',
        'UPI',
        'Net Banking',
        'Wallet'
    ) NOT NULL,

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- ============================
    -- CHECK Constraints
    -- ============================

    CONSTRAINT chk_quantity
        CHECK (Quantity > 0),

    CONSTRAINT chk_discount
        CHECK (DiscountAmount >= 0),

    CONSTRAINT chk_unitprice
        CHECK (UnitPrice > 0),

    CONSTRAINT chk_salesamount
        CHECK (SalesAmount >= 0),

    CONSTRAINT chk_costamount
        CHECK (CostAmount >= 0),

    -- ============================
    -- Foreign Keys
    -- ============================

    CONSTRAINT FK_Sales_Customer
        FOREIGN KEY (CustomerID)
        REFERENCES DimCustomer(CustomerID),

    CONSTRAINT FK_Sales_Product
        FOREIGN KEY (ProductID)
        REFERENCES DimProduct(ProductID),

    CONSTRAINT FK_Sales_Store
        FOREIGN KEY (StoreID)
        REFERENCES DimStore(StoreID),

    CONSTRAINT FK_Sales_Date
        FOREIGN KEY (DateID)
        REFERENCES DimDate(DateID)

);