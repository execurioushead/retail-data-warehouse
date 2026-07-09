-- Stored procedures will be created here.

/*
==========================================================
Retail Sales Data Warehouse
File: 06_procedures.sql

Description:
Stored Procedures for Business Reporting

Author: Rayan Prabhu
==========================================================
*/

USE RetailDW;

-- =====================================================
-- Remove Existing Procedures
-- =====================================================

DROP PROCEDURE IF EXISTS GetMonthlySales;
DROP PROCEDURE IF EXISTS GetTopProducts;
DROP PROCEDURE IF EXISTS GetStorePerformance;
DROP PROCEDURE IF EXISTS GetCustomerSummary;
DROP PROCEDURE IF EXISTS GetRevenueByCategory;

DELIMITER $$

-- =====================================================
-- Procedure 1
-- Monthly Sales for a Given Year
-- =====================================================

CREATE PROCEDURE GetMonthlySales(IN pYear INT)
BEGIN

    SELECT
        YearNumber,
        MonthNumber,
        MonthName,
        Revenue,
        Profit,
        TotalOrders
    FROM vw_MonthlySales
    WHERE YearNumber = pYear
    ORDER BY MonthNumber;

END $$

-- =====================================================
-- Procedure 2
-- Top N Products
-- =====================================================

CREATE PROCEDURE GetTopProducts(IN pLimit INT)
BEGIN

    SELECT
        ProductCode,
        ProductName,
        Category,
        Revenue,
        Profit,
        UnitsSold
    FROM vw_ProductPerformance
    ORDER BY Revenue DESC
    LIMIT pLimit;

END $$

-- =====================================================
-- Procedure 3
-- Store Performance
-- =====================================================

CREATE PROCEDURE GetStorePerformance(IN pStoreID INT)
BEGIN

    SELECT
        StoreID,
        StoreName,
        Region,
        StoreType,
        Orders,
        UnitsSold,
        Revenue,
        Profit
    FROM vw_StorePerformance
    WHERE StoreID = pStoreID;

END $$

-- =====================================================
-- Procedure 4
-- Customer Summary
-- =====================================================

CREATE PROCEDURE GetCustomerSummary(IN pCustomerID INT)
BEGIN

    SELECT
        CustomerID,
        CustomerCode,
        CustomerName,
        LoyaltyTier,
        Orders,
        Revenue,
        Profit
    FROM vw_CustomerSales
    WHERE CustomerID = pCustomerID;

END $$

-- =====================================================
-- Procedure 5
-- Revenue by Category
-- =====================================================

CREATE PROCEDURE GetRevenueByCategory()
BEGIN

    SELECT
        Category,
        Orders,
        UnitsSold,
        Revenue,
        Profit
    FROM vw_CategoryPerformance
    ORDER BY Revenue DESC;

END $$

DELIMITER ;


