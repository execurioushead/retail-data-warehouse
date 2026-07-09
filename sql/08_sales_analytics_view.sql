/*
==========================================================
Retail Sales Data Warehouse
File: 08_sales_analytics_view.sql

Description:
Creates a denormalized analytics view for
Power BI reporting.

Author: Rayan Prabhu
==========================================================
*/

USE RetailDW;

DROP VIEW IF EXISTS vw_SalesAnalytics;

CREATE VIEW vw_SalesAnalytics AS

SELECT

    -- =========================================
    -- Sales
    -- =========================================

    f.SaleID,

    f.Quantity,

    f.UnitPrice,

    f.DiscountAmount,

    f.SalesAmount,

    f.CostAmount,

    f.ProfitAmount,

    f.PaymentMethod,

    -- =========================================
    -- Customer
    -- =========================================

    c.CustomerID,

    c.CustomerCode,

    CONCAT(c.FirstName,' ',c.LastName) AS CustomerName,

    c.Gender,

    c.Age,

    c.Email,

    c.City,

    c.State,

    c.Country,

    c.LoyaltyTier,

    c.JoinDate,

    -- =========================================
    -- Product
    -- =========================================

    p.ProductID,

    p.ProductCode,

    p.ProductName,

    p.Category,

    p.SubCategory,

    p.Brand,

    p.Supplier,

    p.CostPrice,

    p.SellingPrice,

    p.IsActive,

    -- =========================================
    -- Store
    -- =========================================

    s.StoreID,

    s.StoreCode,

    s.StoreName,

    s.StoreType,

    s.Region,

    s.StoreSize,

    s.City AS StoreCity,

    s.State AS StoreState,

    s.Country AS StoreCountry,

    s.OpeningDate,

    -- =========================================
    -- Date
    -- =========================================

    d.DateID,

    d.FullDate,

    d.DayNumber,

    d.MonthNumber,

    d.MonthName,

    d.QuarterNumber,

    d.YearNumber,

    d.WeekdayName,

    d.IsWeekend

FROM FactSales f

INNER JOIN DimCustomer c
ON f.CustomerID = c.CustomerID

INNER JOIN DimProduct p
ON f.ProductID = p.ProductID

INNER JOIN DimStore s
ON f.StoreID = s.StoreID

INNER JOIN DimDate d
ON f.DateID = d.DateID;

