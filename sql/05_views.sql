-- Analytical views will be created here.

/*
==========================================================
Retail Sales Data Warehouse
File: 05_views.sql
==========================================================
*/

USE RetailDW;

DROP VIEW IF EXISTS vw_MonthlySales;

CREATE VIEW vw_MonthlySales AS

SELECT

    d.YearNumber,

    d.MonthNumber,

    d.MonthName,

    COUNT(f.SaleID) AS TotalOrders,

    SUM(f.Quantity) AS TotalItems,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimDate d

ON f.DateID = d.DateID

GROUP BY

    d.YearNumber,

    d.MonthNumber,

    d.MonthName;

DROP VIEW IF EXISTS vw_ProductPerformance;

CREATE VIEW vw_ProductPerformance AS

SELECT

    p.ProductID,

    p.ProductCode,

    p.ProductName,

    p.Category,

    p.Brand,

    COUNT(f.SaleID) AS Orders,

    SUM(f.Quantity) AS UnitsSold,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimProduct p

ON f.ProductID = p.ProductID

GROUP BY

    p.ProductID,

    p.ProductCode,

    p.ProductName,

    p.Category,

    p.Brand;

DROP VIEW IF EXISTS vw_StorePerformance;

CREATE VIEW vw_StorePerformance AS

SELECT

    s.StoreID,

    s.StoreName,

    s.Region,

    s.StoreType,

    COUNT(f.SaleID) AS Orders,

    SUM(f.Quantity) AS UnitsSold,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimStore s

ON f.StoreID = s.StoreID

GROUP BY

    s.StoreID,

    s.StoreName,

    s.Region,

    s.StoreType;

DROP VIEW IF EXISTS vw_CustomerSales;

CREATE VIEW vw_CustomerSales AS

SELECT

    c.CustomerID,

    c.CustomerCode,

    CONCAT(c.FirstName,' ',c.LastName) AS CustomerName,

    c.LoyaltyTier,

    COUNT(f.SaleID) AS Orders,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimCustomer c

ON f.CustomerID = c.CustomerID

GROUP BY

    c.CustomerID,

    c.CustomerCode,

    CustomerName,

    c.LoyaltyTier;

DROP VIEW IF EXISTS vw_CategoryPerformance;

CREATE VIEW vw_CategoryPerformance AS

SELECT

    p.Category,

    COUNT(f.SaleID) AS Orders,

    SUM(f.Quantity) AS UnitsSold,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimProduct p

ON f.ProductID=p.ProductID

GROUP BY

    p.Category;

DROP VIEW IF EXISTS vw_DailySales;

CREATE VIEW vw_DailySales AS

SELECT

    d.FullDate,

    COUNT(f.SaleID) AS Orders,

    SUM(f.Quantity) AS UnitsSold,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimDate d

ON f.DateID=d.DateID

GROUP BY

    d.FullDate;


