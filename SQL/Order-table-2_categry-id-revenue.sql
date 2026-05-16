-- ASSIMENT-2
use dbt;
CREATE TABLE Orders (
OrderID INT PRIMARY KEY,
CustomerID VARCHAR(10),
Category VARCHAR(50),
OrderDate DATE,
OrderValue DECIMAL(10,2)
);
INSERT INTO Orders (OrderID, CustomerID, Category, OrderDate, OrderValue) VALUES
(1001, 'C201', 'Electronics', '2024-01-05', 12500),
(1002, 'C203', 'Apparel', '2024-01-07', 3200),
(1003, 'C205', 'Home', '2024-01-10', 5800),
(1004, 'C201', 'Electronics', '2024-01-15', 8900),
(1005, 'C207', 'Apparel', '2024-01-18', 2100),
(1006, 'C210', 'Home', '2024-01-22', 4700),
(1007, 'C203', 'Electronics', '2024-02-01', 15300),
(1008, 'C212', 'Apparel', '2024-02-05', 1800),
(1009, 'C205', 'Home', '2024-02-08', 6200),
(1010, 'C214', 'Electronics', '2024-02-12', 9400),
(1011, 'C207', 'Apparel', '2024-02-17', 2900),
(1012, 'C210', 'Electronics', '2024-02-20', 11000),
(1013, 'C212', 'Home', '2024-03-01', 3500),
(1014, 'C201', 'Apparel', '2024-03-05', 4100),
(1015, 'C214', 'Home', '2024-03-10', 7800);
-- Level 1 Solutions — Basic GROUP BY
-- Q1. Total Revenue per Category
SELECT Category,SUM(OrderValue) AS Total_Revenue FROM Sales_Data 
GROUP BY Category ORDER BY Total_Revenue DESC;

-- Q2. Total Orders per Category
SELECT Category,COUNT(OrderID) AS Total_Orders FROM Sales_Data 
GROUP BY Category ORDER BY Total_Orders DESC;

-- Q3. Max Order Value per Category
SELECT Category, MAX(OrderValue) AS Max_OrderValue FROM Sales_Data 
GROUP BY Category ORDER BY Max_OrderValue DESC;

-- Level 2 Solutions — DISTINCT
-- Q1. Unique Categories
SELECT DISTINCT Category FROM Sales_Data ORDER BY Category;

-- Q2. Unique CustomerIDs
SELECT DISTINCT CustomerID FROM Sales_Data ORDER BY CustomerID;

-- Q3. Unique Customer + Category Combinations
SELECT DISTINCT CustomerID,Category FROM Sales_Data ORDER BY CustomerID, Category;

-- Level 3 Solutions — GROUP BY Multiple Columns
-- Q1. Revenue by CustomerID and Category
SELECT CustomerID,Category,SUM(OrderValue) AS Total_Revenue FROM Sales_Data 
GROUP BY CustomerID, Category ORDER BY CustomerID, Category;

-- Q2. Order Count by CustomerID and Category
SELECT CustomerID,Category,COUNT(OrderID) AS Order_Count FROM Sales_Data 
GROUP BY CustomerID, Category ORDER BY CustomerID, Category;

-- Q3. Revenue by Category and Month
SELECT Category,MONTH(OrderDate) AS Order_Month,SUM(OrderValue) AS Total_Revenue FROM Sales_Data 
GROUP BY Category, MONTH(OrderDate) ORDER BY Order_Month, Category;

-- Level 4 Solutions — GROUP BY with HAVING
-- Q1. Categories with Revenue > $20,000
SELECT Category,SUM(OrderValue) AS Total_Revenue FROM Sales_Data 
GROUP BY Category HAVING SUM(OrderValue) > 20000 ORDER BY Total_Revenue DESC;

-- Q2. Customers with More Than 1 Order
SELECT CustomerID,COUNT(OrderID) AS Order_Count FROM Sales_Data 
GROUP BY CustomerID HAVING COUNT(OrderID) > 1 ORDER BY Order_Count DESC;

-- Q3. Customer + Category Spending > $10,000
SELECT CustomerID,Category,SUM(OrderValue) AS Total_Spent FROM Sales_Data 
GROUP BY CustomerID, Category HAVING SUM(OrderValue) > 10000 ORDER BY Total_Spent DESC;

-- Level 5 Solutions — Advanced Multi-Function Queries
-- Q1. Category KPI Dashboard (Avg > $5,000)
SELECT Category,COUNT(OrderID) AS Total_Orders,SUM(OrderValue) AS Total_Revenue,ROUND(AVG(OrderValue), 2) AS Avg_OrderValue
FROM Sales_Data GROUP BY Category HAVING AVG(OrderValue) > 5000 ORDER BY Total_Revenue DESC;

-- Q2. High-Value Repeat Customers
SELECT CustomerID,COUNT(OrderID) AS Order_Count,ROUND(AVG(OrderValue), 2) AS Avg_OrderValue FROM Sales_Data
GROUP BY CustomerID HAVING COUNT(OrderID) > 1 AND AVG(OrderValue) > 6000 ORDER BY Avg_OrderValue DESC;

-- Q3. Category-Month Performance (Min 2 Orders)
SELECT Category,MONTH(OrderDate) AS Order_Month,COUNT(OrderID) AS Total_Orders,SUM(OrderValue) AS Total_Revenue,ROUND(AVG(OrderValue), 2) AS Avg_OrderValue FROM Sales_Data
GROUP BY Category, MONTH(OrderDate) HAVING COUNT(OrderID) >= 2 ORDER BY Order_Month ASC, Total_Revenue DESC;

