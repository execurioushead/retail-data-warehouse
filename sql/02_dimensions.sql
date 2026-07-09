-- Dimension tables will be created here.

/*
==========================================================
Retail Sales Data Warehouse
File: 02_dimensions.sql
Description:
Creates all Dimension Tables

Author: Rayan Prabhu
==========================================================
*/

USE RetailDW;
DROP TABLE IF EXISTS DimCustomer;
DROP TABLE IF EXISTS DimProduct;
DROP TABLE IF EXISTS DimStore;
DROP TABLE IF EXISTS DimDate;

-- ==========================================
-- Dimension : Customer
-- ==========================================

CREATE TABLE DimCustomer (

    CustomerID INT AUTO_INCREMENT PRIMARY KEY,

    CustomerCode VARCHAR(12) NOT NULL UNIQUE,

    FirstName VARCHAR(50) NOT NULL,

    LastName VARCHAR(50) NOT NULL,

    Gender ENUM('Male','Female','Other') NOT NULL,

    Age TINYINT UNSIGNED NOT NULL,

    Email VARCHAR(150) NOT NULL UNIQUE,

    City VARCHAR(100) NOT NULL,

    State VARCHAR(100) NOT NULL,

    Country VARCHAR(100) NOT NULL,

    LoyaltyTier ENUM(
        'Bronze',
        'Silver',
        'Gold',
        'Platinum'
    ) NOT NULL DEFAULT 'Bronze',

    JoinDate DATE NOT NULL,

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_customer_age
        CHECK (Age BETWEEN 18 AND 100)

);
-- ==========================================
-- Dimension : Product
-- ==========================================

CREATE TABLE DimProduct (

    ProductID INT AUTO_INCREMENT PRIMARY KEY,

    ProductCode VARCHAR(12) NOT NULL UNIQUE,

    ProductName VARCHAR(150) NOT NULL,

    Category VARCHAR(100) NOT NULL,

    SubCategory VARCHAR(100) NOT NULL,

    Brand VARCHAR(100) NOT NULL,

    Supplier VARCHAR(150) NOT NULL,

    CostPrice DECIMAL(10,2) NOT NULL,

    SellingPrice DECIMAL(10,2) NOT NULL,

    IsActive BOOLEAN NOT NULL DEFAULT TRUE,

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT chk_costprice
        CHECK (CostPrice > 0),

    CONSTRAINT chk_sellingprice
        CHECK (SellingPrice > 0)

);

-- ==========================================
-- Dimension : Store
-- ==========================================

CREATE TABLE DimStore (

    StoreID INT AUTO_INCREMENT PRIMARY KEY,

    StoreCode VARCHAR(10) NOT NULL UNIQUE,

    StoreName VARCHAR(100) NOT NULL,

    StoreType ENUM(
        'Mall',
        'Standalone',
        'Supermarket',
        'Outlet'
    ) NOT NULL,

    Region ENUM(
        'North',
        'South',
        'East',
        'West'
    ) NOT NULL,

    StoreSize ENUM(
        'Small',
        'Medium',
        'Large'
    ) NOT NULL,

    City VARCHAR(100) NOT NULL,

    State VARCHAR(100) NOT NULL,

    Country VARCHAR(100) NOT NULL,

    OpeningDate DATE NOT NULL,

    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
-- ==========================================
-- Dimension : Date
-- ==========================================

CREATE TABLE DimDate (

    DateID INT PRIMARY KEY,

    FullDate DATE NOT NULL UNIQUE,

    DayNumber TINYINT NOT NULL,

    MonthNumber TINYINT NOT NULL,

    MonthName VARCHAR(20) NOT NULL,

    QuarterNumber TINYINT NOT NULL,

    YearNumber SMALLINT NOT NULL,

    WeekdayName VARCHAR(20) NOT NULL,

    IsWeekend BOOLEAN NOT NULL

);

