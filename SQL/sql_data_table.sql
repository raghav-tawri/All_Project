CREATE TABLE Sales_Data (
    OrderID     INT PRIMARY KEY,
    CustomerID  VARCHAR(10),
    Category    VARCHAR(50),
    OrderDate   DATE,
    OrderValue  DECIMAL(10, 2)
);

INSERT INTO Sales_Data (OrderID, CustomerID, Category, OrderDate, OrderValue)
VALUES
    (1002, 'C203', 'Apparel',     '2024-01-07',  3200),
    (1003, 'C205', 'Home',        '2024-01-10',  5800),
    (1004, 'C201', 'Electronic', '2024-01-15',  8900),
    (1005, 'C207', 'Apparel',     '2024-01-18',  2100),
    (1006, 'C210', 'Home',        '2024-01-22',  4700),
    (1007, 'C203', 'Electronic', '2024-02-01', 15300),
    (1008, 'C212', 'Apparel',     '2024-02-05',  1800),
    (1009, 'C205', 'Home',        '2024-02-08',  6200),
    (1010, 'C214', 'Electronic', '2024-02-12',  9400),
    (1011, 'C207', 'Apparel',     '2024-02-17',  2900),
    (1012, 'C210', 'Electronic', '2024-02-20', 11000),
    (1013, 'C212', 'Home',        '2024-03-01',  3500),
    (1014, 'C201', 'Apparel',     '2024-03-05',  4100),
    (1015, 'C214', 'Home',        '2024-03-10',  7800);
SELECT * from Sales_Data;

-- LEVEL-1(Easy)
-- Q1 — Total revenue per category
select Category, sum(OrderValue) AS Total_Revenue from sales_Data 
GROUP BY Category ORDER BY Total_Revenue DESC;
--  Q2 — Total orders per category
select Category, COUNT(OrderID) AS Total_Orders from Sales_Data 
GROUP BY Category ORDER BY Total_Orders DESC;
--  Q3 — Max order value per category
select Category, MAX(OrderValue) AS Max_OrderValue from Sales_Data 
GROUP BY Category ORDER BY Max_OrderValue DESC;

-- LEVEL-2(Easy)
-- Q1 — Unique categories
select DISTINCT Category from Sales_Data ORDER BY Category;
-- Q2 — Unique customer IDs
select DISTINCT CustomerID from Sales_Data ORDER BY CustomerID;
-- Q3 — Unique customer + category combinations
select DISTINCT CustomerID,Category from Sales_Data ORDER BY CustomerID, Category;

-- LEVEl-3(MED)
-- Q1 — Revenue by CustomerID and Category
select CustomerID,Category,SUM(OrderValue) AS Total_Revenue from Sales_Data
GROUP BY CustomerID, Category ORDER BY CustomerID, Category;
-- Q2 — Order count by CustomerID and Category
select CustomerID,Category,COUNT(OrderID) AS Order_Count from Sales_Data
GROUP BY CustomerID, Category ORDER BY CustomerID, Category;
-- Q3 — Revenue by Category and Month
select Category,MONTH(OrderDate) AS Order_Month,SUM(OrderValue)  AS Total_Revenue from Sales_Data
GROUP BY Category, MONTH(OrderDate) ORDER BY Order_Month, Category;

-- LEVEL-4(MID)
-- Q1 — Categories with revenue > $20,000
select Category,SUM(OrderValue) AS Total_Revenue from Sales_Data
GROUP BY Category HAVING SUM(OrderValue) > 20000 ORDER BY Total_Revenue DESC;
-- Q2 — Customers with more than 1 order
select CustomerID,COUNT(OrderID) AS Order_Count from Sales_Data
GROUP BY CustomerID HAVING COUNT(OrderID) > 1 ORDER BY Order_Count DESC;
-- Q3 — Customer + Category spending > $10,000
select CustomerID,Category,SUM(OrderValue) AS Total_Spent from Sales_Data
GROUP BY CustomerID, Category HAVING SUM(OrderValue) > 10000 ORDER BY Total_Spent DESC;

-- LEVEL-5(HARD)
-- Q1 — Category KPI dashboard (avg order value > $5,000)
select Category,COUNT(OrderID)AS Total_Orders,SUM(OrderValue)AS Total_Revenue,ROUND(AVG(OrderValue),2)AS Avg_OrderValue from Sales_Data
GROUP BY Category HAVING AVG(OrderValue) > 5000 ORDER BY Total_Revenue DESC;
-- Q2 — High-value repeat customers (>1 order AND avg > $6,000)
select CustomerID,COUNT(OrderID)AS Order_Count,ROUND(AVG(OrderValue),2)AS Avg_OrderValue from Sales_Data
GROUP BY CustomerID HAVING COUNT(OrderID) > 1 AND AVG(OrderValue) > 6000 ORDER BY Avg_OrderValue DESC;
-- Q3 — Category-month summary (min 2 orders, sorted by month then revenue)
select Category,MONTH(OrderDate)AS Order_Month,COUNT(OrderID)AS Total_Orders,SUM(OrderValue)AS Total_Revenue,ROUND(AVG(OrderValue),2)AS Avg_OrderValue from Sales_Data
GROUP BY Category, MONTH(OrderDate) HAVING COUNT(OrderID) >= 2 ORDER BY Order_Month ASC, Total_Revenue DESC;



