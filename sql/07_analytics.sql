-- Business analytics queries will be created here.

/*
==========================================================
Retail Sales Data Warehouse
File: 07_analytics.sql

Description:
Business Analytics Queries

Author: Rayan Prabhu
==========================================================
*/

USE RetailDW;

-- =====================================================
-- MODULE 1
-- EXECUTIVE KPIs
-- =====================================================

-- ==============================================
-- KPI 1
-- Total Revenue
-- ==============================================

SELECT
    ROUND(SUM(SalesAmount),2) AS TotalRevenue
FROM FactSales;


-- ==============================================
-- KPI 2
-- Total Profit
-- ==============================================

SELECT
    ROUND(SUM(ProfitAmount),2) AS TotalProfit
FROM FactSales;


-- ==============================================
-- KPI 3
-- Total Orders
-- ==============================================

SELECT
    COUNT(*) AS TotalOrders
FROM FactSales;


-- ==============================================
-- KPI 4
-- Total Quantity Sold
-- ==============================================

SELECT
    SUM(Quantity) AS TotalUnitsSold
FROM FactSales;


-- ==============================================
-- KPI 5
-- Average Order Value
-- ==============================================

SELECT
    ROUND(AVG(SalesAmount),2) AS AverageOrderValue
FROM FactSales;


-- ==============================================
-- KPI 6
-- Average Profit Per Order
-- ==============================================

SELECT
    ROUND(AVG(ProfitAmount),2) AS AverageProfitPerOrder
FROM FactSales;


-- ==============================================
-- KPI 7
-- Highest Order Value
-- ==============================================

SELECT
    MAX(SalesAmount) AS HighestOrder
FROM FactSales;


-- ==============================================
-- KPI 8
-- Lowest Order Value
-- ==============================================

SELECT
    MIN(SalesAmount) AS LowestOrder
FROM FactSales;


-- ==============================================
-- KPI 9
-- Total Customers
-- ==============================================

SELECT
    COUNT(*) AS TotalCustomers
FROM DimCustomer;


-- ==============================================
-- KPI 10
-- Total Products
-- ==============================================

SELECT
    COUNT(*) AS TotalProducts
FROM DimProduct;


-- =====================================================
-- MODULE 2
-- CUSTOMER ANALYTICS
-- =====================================================

-- ==============================================
-- CUSTOMER 1
-- Top 10 Customers by Revenue
-- ==============================================

SELECT
    CustomerCode,
    CustomerName,
    LoyaltyTier,
    Revenue
FROM vw_CustomerSales
ORDER BY Revenue DESC
LIMIT 10;


-- ==============================================
-- CUSTOMER 2
-- Top 10 Customers by Profit
-- ==============================================

SELECT
    CustomerCode,
    CustomerName,
    LoyaltyTier,
    Profit
FROM vw_CustomerSales
ORDER BY Profit DESC
LIMIT 10;


-- ==============================================
-- CUSTOMER 3
-- Top 10 Customers by Number of Orders
-- ==============================================

SELECT
    CustomerCode,
    CustomerName,
    Orders
FROM vw_CustomerSales
ORDER BY Orders DESC
LIMIT 10;


-- ==============================================
-- CUSTOMER 4
-- Revenue by Loyalty Tier
-- ==============================================

SELECT

    LoyaltyTier,

    COUNT(*) AS Customers,

    ROUND(SUM(Revenue),2) AS Revenue,

    ROUND(AVG(Revenue),2) AS AverageRevenue

FROM vw_CustomerSales

GROUP BY LoyaltyTier

ORDER BY Revenue DESC;


-- ==============================================
-- CUSTOMER 5
-- Average Spend Per Customer
-- ==============================================

SELECT

    ROUND(AVG(Revenue),2) AS AverageCustomerSpend

FROM vw_CustomerSales;


-- ==============================================
-- CUSTOMER 6
-- Revenue by State
-- ==============================================

SELECT

    c.State,

    COUNT(DISTINCT c.CustomerID) AS Customers,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimCustomer c

ON f.CustomerID = c.CustomerID

GROUP BY c.State

ORDER BY Revenue DESC;


-- ==============================================
-- CUSTOMER 7
-- Revenue by City
-- ==============================================

SELECT

    c.City,

    COUNT(DISTINCT c.CustomerID) AS Customers,

    ROUND(SUM(f.SalesAmount),2) AS Revenue

FROM FactSales f

JOIN DimCustomer c

ON f.CustomerID = c.CustomerID

GROUP BY c.City

ORDER BY Revenue DESC

LIMIT 15;


-- ==============================================
-- CUSTOMER 8
-- Customers Joined Each Year
-- ==============================================

SELECT

    YEAR(JoinDate) AS JoinYear,

    COUNT(*) AS NewCustomers

FROM DimCustomer

GROUP BY YEAR(JoinDate)

ORDER BY JoinYear;


-- ==============================================
-- CUSTOMER 9
-- Customer Revenue Ranking
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    Revenue,

    RANK() OVER(

        ORDER BY Revenue DESC

    ) AS CustomerRank

FROM vw_CustomerSales;


-- ==============================================
-- CUSTOMER 10
-- Top Gold & Platinum Customers
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    LoyaltyTier,

    Revenue

FROM vw_CustomerSales

WHERE LoyaltyTier IN ('Gold','Platinum')

ORDER BY Revenue DESC

LIMIT 20;


-- =====================================================
-- MODULE 3
-- PRODUCT ANALYTICS
-- =====================================================

-- ==============================================
-- PRODUCT 1
-- Top 10 Products by Revenue
-- ==============================================

SELECT
    ProductCode,
    ProductName,
    Category,
    Brand,
    Revenue
FROM vw_ProductPerformance
ORDER BY Revenue DESC
LIMIT 10;


-- ==============================================
-- PRODUCT 2
-- Top 10 Products by Profit
-- ==============================================

SELECT
    ProductCode,
    ProductName,
    Category,
    Profit
FROM vw_ProductPerformance
ORDER BY Profit DESC
LIMIT 10;


-- ==============================================
-- PRODUCT 3
-- Top 10 Best Selling Products
-- ==============================================

SELECT
    ProductCode,
    ProductName,
    UnitsSold
FROM vw_ProductPerformance
ORDER BY UnitsSold DESC
LIMIT 10;


-- ==============================================
-- PRODUCT 4
-- Bottom 10 Products by Revenue
-- ==============================================

SELECT
    ProductCode,
    ProductName,
    Revenue
FROM vw_ProductPerformance
ORDER BY Revenue ASC
LIMIT 10;


-- ==============================================
-- PRODUCT 5
-- Revenue by Category
-- ==============================================

SELECT
    Category,
    Orders,
    UnitsSold,
    Revenue,
    Profit
FROM vw_CategoryPerformance
ORDER BY Revenue DESC;


-- ==============================================
-- PRODUCT 6
-- Revenue by Brand
-- ==============================================

SELECT

    Brand,

    COUNT(*) AS Products,

    ROUND(SUM(Revenue),2) AS Revenue,

    ROUND(SUM(Profit),2) AS Profit

FROM vw_ProductPerformance

GROUP BY Brand

ORDER BY Revenue DESC;


-- ==============================================
-- PRODUCT 7
-- Revenue by Supplier
-- ==============================================

SELECT

    p.Supplier,

    COUNT(*) AS Products,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimProduct p

ON f.ProductID = p.ProductID

GROUP BY p.Supplier

ORDER BY Revenue DESC;


-- ==============================================
-- PRODUCT 8
-- Average Selling Price by Category
-- ==============================================

SELECT

    Category,

    ROUND(AVG(SellingPrice),2) AS AvgSellingPrice,

    ROUND(AVG(CostPrice),2) AS AvgCostPrice

FROM DimProduct

GROUP BY Category

ORDER BY AvgSellingPrice DESC;


-- ==============================================
-- PRODUCT 9
-- Active vs Inactive Products
-- ==============================================

SELECT

    IsActive,

    COUNT(*) AS TotalProducts

FROM DimProduct

GROUP BY IsActive;


-- ==============================================
-- PRODUCT 10
-- Product Revenue Ranking
-- ==============================================

SELECT

    ProductCode,

    ProductName,

    Revenue,

    RANK() OVER(

        ORDER BY Revenue DESC

    ) AS RevenueRank

FROM vw_ProductPerformance;


-- =====================================================
-- MODULE 4
-- STORE ANALYTICS
-- =====================================================

-- ==============================================
-- STORE 1
-- Top 10 Stores by Revenue
-- ==============================================

SELECT
    StoreID,
    StoreName,
    Region,
    StoreType,
    Revenue
FROM vw_StorePerformance
ORDER BY Revenue DESC
LIMIT 10;


-- ==============================================
-- STORE 2
-- Top 10 Stores by Profit
-- ==============================================

SELECT
    StoreID,
    StoreName,
    Region,
    Profit
FROM vw_StorePerformance
ORDER BY Profit DESC
LIMIT 10;


-- ==============================================
-- STORE 3
-- Best Stores by Units Sold
-- ==============================================

SELECT
    StoreID,
    StoreName,
    UnitsSold
FROM vw_StorePerformance
ORDER BY UnitsSold DESC
LIMIT 10;


-- ==============================================
-- STORE 4
-- Revenue by Region
-- ==============================================

SELECT

    Region,

    COUNT(*) AS Stores,

    ROUND(SUM(Revenue),2) AS Revenue,

    ROUND(SUM(Profit),2) AS Profit

FROM vw_StorePerformance

GROUP BY Region

ORDER BY Revenue DESC;


-- ==============================================
-- STORE 5
-- Revenue by Store Type
-- ==============================================

SELECT

    StoreType,

    COUNT(*) AS Stores,

    ROUND(SUM(Revenue),2) AS Revenue,

    ROUND(SUM(Profit),2) AS Profit

FROM vw_StorePerformance

GROUP BY StoreType

ORDER BY Revenue DESC;


-- ==============================================
-- STORE 6
-- Average Revenue per Store
-- ==============================================

SELECT

    ROUND(AVG(Revenue),2) AS AverageRevenuePerStore,

    ROUND(AVG(Profit),2) AS AverageProfitPerStore

FROM vw_StorePerformance;


-- ==============================================
-- STORE 7
-- Store Ranking by Revenue
-- ==============================================

SELECT

    StoreName,

    Revenue,

    RANK() OVER(
        ORDER BY Revenue DESC
    ) AS RevenueRank

FROM vw_StorePerformance;


-- ==============================================
-- STORE 8
-- Revenue by Store Size
-- ==============================================

SELECT

    s.StoreSize,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimStore s

ON f.StoreID = s.StoreID

GROUP BY s.StoreSize

ORDER BY Revenue DESC;


-- ==============================================
-- STORE 9
-- Number of Stores by Region
-- ==============================================

SELECT

    Region,

    COUNT(*) AS TotalStores

FROM DimStore

GROUP BY Region

ORDER BY TotalStores DESC;


-- ==============================================
-- STORE 10
-- Oldest Stores
-- ==============================================

SELECT

    StoreCode,

    StoreName,

    OpeningDate

FROM DimStore

ORDER BY OpeningDate

LIMIT 10;


-- =====================================================
-- MODULE 5
-- TIME INTELLIGENCE
-- =====================================================

-- ==============================================
-- TIME 1
-- Monthly Revenue Trend
-- ==============================================

SELECT
    YearNumber,
    MonthNumber,
    MonthName,
    Revenue,
    Profit
FROM vw_MonthlySales
ORDER BY YearNumber, MonthNumber;


-- ==============================================
-- TIME 2
-- Revenue by Year
-- ==============================================

SELECT

    d.YearNumber,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit,

    COUNT(f.SaleID) AS Orders

FROM FactSales f

JOIN DimDate d
ON f.DateID = d.DateID

GROUP BY d.YearNumber

ORDER BY d.YearNumber;


-- ==============================================
-- TIME 3
-- Revenue by Quarter
-- ==============================================

SELECT

    d.YearNumber,

    d.QuarterNumber,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimDate d
ON f.DateID = d.DateID

GROUP BY
    d.YearNumber,
    d.QuarterNumber

ORDER BY
    d.YearNumber,
    d.QuarterNumber;


-- ==============================================
-- TIME 4
-- Best Sales Month
-- ==============================================

SELECT

    YearNumber,

    MonthName,

    Revenue

FROM vw_MonthlySales

ORDER BY Revenue DESC

LIMIT 10;


-- ==============================================
-- TIME 5
-- Best Sales Quarter
-- ==============================================

SELECT

    d.YearNumber,

    d.QuarterNumber,

    ROUND(SUM(f.SalesAmount),2) AS Revenue

FROM FactSales f

JOIN DimDate d
ON f.DateID = d.DateID

GROUP BY
    d.YearNumber,
    d.QuarterNumber

ORDER BY Revenue DESC

LIMIT 10;


-- ==============================================
-- TIME 6
-- Weekend vs Weekday Sales
-- ==============================================

SELECT

    CASE

        WHEN d.IsWeekend = TRUE
        THEN 'Weekend'

        ELSE 'Weekday'

    END AS DayType,

    COUNT(*) AS Orders,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimDate d
ON f.DateID = d.DateID

GROUP BY DayType;


-- ==============================================
-- TIME 7
-- Revenue by Weekday
-- ==============================================

SELECT

    d.WeekdayName,

    ROUND(SUM(f.SalesAmount),2) AS Revenue,

    ROUND(SUM(f.ProfitAmount),2) AS Profit

FROM FactSales f

JOIN DimDate d
ON f.DateID = d.DateID

GROUP BY d.WeekdayName

ORDER BY Revenue DESC;


-- ==============================================
-- TIME 8
-- Average Daily Revenue
-- ==============================================

SELECT

    ROUND(AVG(Revenue),2) AS AverageDailyRevenue,

    ROUND(AVG(Profit),2) AS AverageDailyProfit

FROM vw_DailySales;


-- ==============================================
-- TIME 9
-- Highest Revenue Day
-- ==============================================

SELECT

    FullDate,

    Revenue,

    Profit

FROM vw_DailySales

ORDER BY Revenue DESC

LIMIT 10;


-- ==============================================
-- TIME 10
-- Monthly Order Count
-- ==============================================

SELECT

    YearNumber,

    MonthName,

    TotalOrders

FROM vw_MonthlySales

ORDER BY
    YearNumber,
    MonthNumber; 



-- =====================================================
-- MODULE 6
-- PAYMENT ANALYTICS
-- =====================================================

-- ==============================================
-- PAYMENT 1
-- Revenue by Payment Method
-- ==============================================

SELECT

    PaymentMethod,

    ROUND(SUM(SalesAmount),2) AS Revenue,

    ROUND(SUM(ProfitAmount),2) AS Profit,

    COUNT(*) AS Orders

FROM FactSales

GROUP BY PaymentMethod

ORDER BY Revenue DESC;


-- ==============================================
-- PAYMENT 2
-- Average Order Value by Payment Method
-- ==============================================

SELECT

    PaymentMethod,

    ROUND(AVG(SalesAmount),2) AS AverageOrderValue,

    ROUND(AVG(ProfitAmount),2) AS AverageProfit

FROM FactSales

GROUP BY PaymentMethod

ORDER BY AverageOrderValue DESC;


-- ==============================================
-- PAYMENT 3
-- Units Sold by Payment Method
-- ==============================================

SELECT

    PaymentMethod,

    SUM(Quantity) AS UnitsSold

FROM FactSales

GROUP BY PaymentMethod

ORDER BY UnitsSold DESC;


-- ==============================================
-- PAYMENT 4
-- Highest Revenue Payment Method
-- ==============================================

SELECT

    PaymentMethod,

    ROUND(SUM(SalesAmount),2) AS Revenue

FROM FactSales

GROUP BY PaymentMethod

ORDER BY Revenue DESC

LIMIT 1;


-- ==============================================
-- PAYMENT 5
-- Payment Method Contribution (%)
-- ==============================================

SELECT

    PaymentMethod,

    ROUND(SUM(SalesAmount),2) AS Revenue,

    ROUND(

        SUM(SalesAmount) * 100 /

        (SELECT SUM(SalesAmount) FROM FactSales),

        2

    ) AS RevenuePercentage

FROM FactSales

GROUP BY PaymentMethod

ORDER BY Revenue DESC;



-- =====================================================
-- MODULE 7
-- WINDOW FUNCTIONS
-- =====================================================

-- ==============================================
-- WINDOW 1
-- Product Revenue Ranking
-- ==============================================

SELECT

    ProductName,

    Revenue,

    RANK() OVER(

        ORDER BY Revenue DESC

    ) AS RevenueRank

FROM vw_ProductPerformance;


-- ==============================================
-- WINDOW 2
-- Dense Ranking
-- ==============================================

SELECT

    ProductName,

    Revenue,

    DENSE_RANK() OVER(

        ORDER BY Revenue DESC

    ) AS DenseRank

FROM vw_ProductPerformance;


-- ==============================================
-- WINDOW 3
-- Row Number
-- ==============================================

SELECT

    ProductName,

    Revenue,

    ROW_NUMBER() OVER(

        ORDER BY Revenue DESC

    ) AS RowNumber

FROM vw_ProductPerformance;


-- ==============================================
-- WINDOW 4
-- Top Product in Each Category
-- ==============================================

SELECT *

FROM(

    SELECT

        ProductName,

        Category,

        Revenue,

        ROW_NUMBER() OVER(

            PARTITION BY Category

            ORDER BY Revenue DESC

        ) AS rn

    FROM vw_ProductPerformance

) t

WHERE rn=1;


-- =====================================================
-- MODULE 8
-- RUNNING TOTALS
-- =====================================================

-- ==============================================
-- RUNNING 1
-- Daily Running Revenue
-- ==============================================

SELECT

    FullDate,

    Revenue,

    SUM(Revenue)

    OVER(

        ORDER BY FullDate

    ) AS RunningRevenue

FROM vw_DailySales;


-- ==============================================
-- RUNNING 2
-- Daily Running Profit
-- ==============================================

SELECT

    FullDate,

    Profit,

    SUM(Profit)

    OVER(

        ORDER BY FullDate

    ) AS RunningProfit

FROM vw_DailySales;


-- ==============================================
-- RUNNING 3
-- 7-Day Moving Average Revenue
-- ==============================================

SELECT

    FullDate,

    Revenue,

    ROUND(

        AVG(Revenue)

        OVER(

            ORDER BY FullDate

            ROWS BETWEEN 6 PRECEDING

            AND CURRENT ROW

        ),

        2

    ) AS MovingAverageRevenue

FROM vw_DailySales;


-- =====================================================
-- MODULE 9
-- CUSTOMER SEGMENTATION
-- =====================================================

-- ==============================================
-- SEGMENT 1
-- Top 20 Customers by Revenue
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    LoyaltyTier,

    Revenue

FROM vw_CustomerSales

ORDER BY Revenue DESC

LIMIT 20;


-- ==============================================
-- SEGMENT 2
-- High Value Customers
-- (Revenue Above Average)
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    Revenue

FROM vw_CustomerSales

WHERE Revenue >

(

    SELECT AVG(Revenue)

    FROM vw_CustomerSales

)

ORDER BY Revenue DESC;


-- ==============================================
-- SEGMENT 3
-- Customer Frequency
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    Orders,

    CASE

        WHEN Orders >= 25 THEN 'Very Frequent'

        WHEN Orders >= 15 THEN 'Frequent'

        WHEN Orders >= 8 THEN 'Regular'

        ELSE 'Occasional'

    END AS CustomerSegment

FROM vw_CustomerSales

ORDER BY Orders DESC;


-- ==============================================
-- SEGMENT 4
-- Loyalty Tier Performance
-- ==============================================

SELECT

    LoyaltyTier,

    COUNT(*) AS Customers,

    ROUND(AVG(Revenue),2) AS AvgRevenue,

    ROUND(AVG(Profit),2) AS AvgProfit,

    ROUND(SUM(Revenue),2) AS TotalRevenue

FROM vw_CustomerSales

GROUP BY LoyaltyTier

ORDER BY TotalRevenue DESC;


-- ==============================================
-- SEGMENT 5
-- VIP Customers
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    Revenue,

    Profit,

    Orders

FROM vw_CustomerSales

WHERE Revenue >

(

    SELECT

        AVG(Revenue) + STDDEV(Revenue)

    FROM vw_CustomerSales

)

ORDER BY Revenue DESC;


-- ==============================================
-- SEGMENT 6
-- RFM Analysis
-- ==============================================

SELECT

    c.CustomerCode,

    CONCAT(c.FirstName,' ',c.LastName) AS CustomerName,

    DATEDIFF(

        MAX(d.FullDate),

        MAX(d.FullDate)

    ) AS Recency,

    COUNT(f.SaleID) AS Frequency,

    ROUND(SUM(f.SalesAmount),2) AS Monetary

FROM FactSales f

JOIN DimCustomer c

ON f.CustomerID = c.CustomerID

JOIN DimDate d

ON f.DateID = d.DateID

GROUP BY

    c.CustomerCode,

    CustomerName

ORDER BY Monetary DESC;


-- ==============================================
-- SEGMENT 7
-- Estimated Customer Lifetime Value
-- ==============================================

SELECT

    CustomerCode,

    CustomerName,

    ROUND(

        Revenue / Orders,

        2

    ) AS AverageOrderValue,

    Orders,

    ROUND(

        Revenue,

        2

    ) AS EstimatedLifetimeValue

FROM vw_CustomerSales

ORDER BY EstimatedLifetimeValue DESC;


-- ==============================================
-- SEGMENT 8
-- Revenue Distribution
-- ==============================================

SELECT

    CASE

        WHEN Revenue >= 50000 THEN 'Premium'

        WHEN Revenue >= 25000 THEN 'High'

        WHEN Revenue >= 10000 THEN 'Medium'

        ELSE 'Low'

    END AS RevenueBand,

    COUNT(*) AS Customers

FROM vw_CustomerSales

GROUP BY RevenueBand

ORDER BY Customers DESC;


-- ==============================================
-- SEGMENT 9
-- Loyalty Ranking
-- ==============================================

SELECT

    CustomerName,

    LoyaltyTier,

    Revenue,

    DENSE_RANK()

    OVER(

        PARTITION BY LoyaltyTier

        ORDER BY Revenue DESC

    ) AS TierRank

FROM vw_CustomerSales;


-- ==============================================
-- SEGMENT 10
-- Best Customer in Each Loyalty Tier
-- ==============================================

SELECT *

FROM(

    SELECT

        CustomerName,

        LoyaltyTier,

        Revenue,

        ROW_NUMBER()

        OVER(

            PARTITION BY LoyaltyTier

            ORDER BY Revenue DESC

        ) AS rn

    FROM vw_CustomerSales

) x

WHERE rn = 1;

-- =====================================================
-- MODULE 10
-- EXECUTIVE BUSINESS INSIGHTS
-- =====================================================

-- ==============================================
-- INSIGHT 1
-- Top 20 Products Generate How Much Revenue?
-- ==============================================

SELECT

    ProductName,

    Revenue,

    ROUND(

        Revenue * 100 /

        (SELECT SUM(Revenue)

        FROM vw_ProductPerformance),

        2

    ) AS RevenuePercentage

FROM vw_ProductPerformance

ORDER BY Revenue DESC

LIMIT 20;


-- ==============================================
-- INSIGHT 2
-- Revenue Contribution by Category
-- ==============================================

SELECT

    Category,

    Revenue,

    ROUND(

        Revenue * 100 /

        (SELECT SUM(Revenue)

        FROM vw_CategoryPerformance),

        2

    ) AS RevenueShare

FROM vw_CategoryPerformance

ORDER BY Revenue DESC;


-- ==============================================
-- INSIGHT 3
-- Most Profitable Category
-- ==============================================

SELECT

    Category,

    Profit

FROM vw_CategoryPerformance

ORDER BY Profit DESC

LIMIT 1;


-- ==============================================
-- INSIGHT 4
-- Most Profitable Region
-- ==============================================

SELECT

    Region,

    Revenue,

    Profit

FROM vw_StorePerformance

ORDER BY Profit DESC

LIMIT 1;


-- ==============================================
-- INSIGHT 5
-- Highest Revenue Brand
-- ==============================================

SELECT

    Brand,

    ROUND(SUM(Revenue),2) AS Revenue,

    ROUND(SUM(Profit),2) AS Profit

FROM vw_ProductPerformance

GROUP BY Brand

ORDER BY Revenue DESC

LIMIT 10;


-- ==============================================
-- INSIGHT 6
-- Supplier Performance
-- ==============================================

SELECT

    Supplier,

    ROUND(SUM(Revenue),2) AS Revenue,

    ROUND(SUM(Profit),2) AS Profit

FROM

(

    SELECT

        p.Supplier,

        f.SalesAmount AS Revenue,

        f.ProfitAmount AS Profit

    FROM FactSales f

    JOIN DimProduct p

    ON f.ProductID = p.ProductID

) x

GROUP BY Supplier

ORDER BY Revenue DESC;


-- ==============================================
-- INSIGHT 7
-- Monthly Growth Percentage
-- ==============================================

SELECT

    YearNumber,

    MonthNumber,

    Revenue,

    LAG(Revenue)

    OVER(

        ORDER BY YearNumber, MonthNumber

    ) AS PreviousRevenue,

    ROUND(

        (

            Revenue -

            LAG(Revenue)

            OVER(

                ORDER BY YearNumber, MonthNumber

            )

        )

        /

        LAG(Revenue)

        OVER(

            ORDER BY YearNumber, MonthNumber

        )

        *100,

        2

    ) AS GrowthPercentage

FROM vw_MonthlySales;


-- ==============================================
-- INSIGHT 8
-- Cumulative Revenue
-- ==============================================

SELECT

    FullDate,

    Revenue,

    SUM(Revenue)

    OVER(

        ORDER BY FullDate

    ) AS RunningRevenue

FROM vw_DailySales;

-- ==============================================
-- INSIGHT 9
-- Top 20% Customers by Revenue
-- ==============================================

WITH RankedCustomers AS
(
    SELECT

        CustomerName,

        CustomerCode,

        Revenue,

        NTILE(5) OVER (
            ORDER BY Revenue DESC
        ) AS RevenueGroup

    FROM vw_CustomerSales
)

SELECT

    CustomerCode,

    CustomerName,

    Revenue

FROM RankedCustomers

WHERE RevenueGroup = 1

ORDER BY Revenue DESC;


-- ==============================================
-- INSIGHT 10
-- Revenue by Customer Decile
-- ==============================================

SELECT

    CustomerName,

    Revenue,

    NTILE(10)

    OVER(

        ORDER BY Revenue DESC

    ) AS RevenueDecile

FROM vw_CustomerSales;





