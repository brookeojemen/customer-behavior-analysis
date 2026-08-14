

/*
SELECT * FROM customer_table LIMIT 5;
PRAGMA table_info(customer_table);
PRAGMA table_info(customer_data_clean);

INSERT INTO customer_data_clean(
    InvoiceNo,
    StockCode,
    Quantity,
    InvoiceDate,
    UnitPrice,
    CustomerID
)
SELECT
    InvoiceNo,
    StockCode,
    CAST(Quantity AS INTEGER),
    InvoiceDate,
    CAST(UnitPrice AS REAL),
    CAST(CustomerID AS REAL) 
FROM customer_table;

DELETE FROM customer_data_clean
WHERE CustomerID = 0;

DELETE FROM customer_data_clean
WHERE Quantity <= 0;

DELETE FROM customer_data_clean
WHERE UnitPrice <= 0;

DELETE FROM customer_data_clean
WHERE StockCode IN ('POST','DOT','D');
*/



SELECT 
    COUNT(*) AS total_rows,
    COUNT(DISTINCT InvoiceNo) AS TotalOrders,
    COUNT(DISTINCT CustomerID) AS TotalCustomers,
    COUNT(DISTINCT StockCode) AS TotalProducts
FROM customer_data_clean;


SELECT
    CustomerID,
    SUM(Quantity * UnitPrice) AS TotalSpent
FROM customer_data_clean
GROUP BY CustomerID
ORDER BY TotalSpent DESC
LIMIT 10;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS TotalOrders
FROM customer_data_clean
GROUP BY CustomerID
ORDER BY TotalOrders DESC
LIMIT 10;

SELECT
    CustomerID,
    COUNT(DISTINCT InvoiceNo) AS TotalOrders,
    SUM(Quantity * UnitPrice) AS TotalSpent,
    SUM(Quantity * UnitPrice) / COUNT(DISTINCT InvoiceNo) AS AverageOrderValue
FROM customer_data_clean
GROUP BY CustomerID
ORDER BY AverageOrderValue DESC
LIMIT 10;

SELECT
    StockCode,
    COUNT(DISTINCT InvoiceNo) AS NumberOfOrders
FROM customer_data_clean
GROUP BY StockCode
ORDER BY NumberOfOrders DESC
LIMIT 10;

SELECT
    StockCode,
    SUM(Quantity) AS TotalQuantitySold
FROM customer_data_clean
GROUP BY StockCode
ORDER BY TotalQuantitySold DESC
LIMIT 10;

SELECT
    StockCode,
    SUM(Quantity * UnitPrice) AS TotalRevenue
FROM customer_data_clean
GROUP BY StockCode
ORDER BY TotalRevenue DESC
LIMIT 10;


SELECT
    InvoiceDate,
    substr(InvoiceDate, 1, instr(InvoiceDate, '/')- 1) AS Month,
    substr(
        InvoiceDate,
        instr(InvoiceDate, '/') + 1,
        instr(substr(InvoiceDate, instr(InvoiceDate, '/') + 1), '/') - 1
    ) AS Day,

     substr(
        InvoiceDate,
        instr(InvoiceDate, '/') +
        instr(substr(InvoiceDate, instr(InvoiceDate, '/') + 1), '/') + 1,
        4
    ) AS Year,

    substr(
        InvoiceDate,
        instr(InvoiceDate, ' ') + 1
    ) AS Time
FROM customer_data_clean
LIMIT 10;

SELECT
    strftime('%Y-%m', InvoiceDateISO) AS Month,
    SUM(Quantity * UnitPrice) AS MonthlyRevenue
FROM customer_data_clean
GROUP BY Month
ORDER BY MonthlyRevenue DESC
LIMIT 1;

SELECT
    CASE strftime('%w', InvoiceDateISO)
        WHEN '0' THEN 'Sunday'
        WHEN '1' THEN 'Monday'
        WHEN '2' THEN 'Tuesday'
        WHEN '3' THEN 'Wednesday'
        WHEN '4' THEN 'Thursday'
        WHEN '5' THEN 'Friday'
        WHEN '6' THEN 'Saturday'
    END AS DayOfWeek,
    SUM(Quantity * UnitPrice) AS TotalRevenue
FROM customer_data_clean
GROUP BY strftime('%w', InvoiceDateISO)
ORDER BY TotalRevenue DESC;

SELECT
    AVG(OrderTotal) AS AverageOrderValue
FROM(
    SELECT
        InvoiceNo,
        SUM(Quantity * UnitPrice) AS OrderTotal
    From customer_data_clean
    GROUP BY InvoiceNo
);

SELECT *
FROM customer_summary
LIMIT 10;


