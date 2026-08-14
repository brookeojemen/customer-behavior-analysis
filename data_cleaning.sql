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