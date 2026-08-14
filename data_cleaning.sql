SELECT * FROM customer_table LIMIT 5;
PRAGMA table_info(customer_table);


DROP TABLE IF EXISTS customer_data_clean;
CREATE TABLE customer_data_clean (
    InvoiceNo TEXT,
    StockCode TEXT,
    Quantity INTEGER,
    InvoiceDate TEXT,
    UnitPrice REAL,
    CustomerID REAL
);

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

ALTER TABLE customer_data_clean
ADD COLUMN InvoiceDateISO TEXT;

UPDATE customer_data_clean
SET InvoiceDateISO =
    substr(
        InvoiceDate,
        instr(InvoiceDate, '/') +
        instr(substr(InvoiceDate, instr(InvoiceDate, '/') + 1), '/') + 1,
        4
    )
    || '-' ||
    printf(
        '%02d',
        CAST(
            substr(
                InvoiceDate,
                1,
                instr(InvoiceDate, '/') - 1
            ) AS INTEGER
        )
    )
    || '-' ||
    printf(
        '%02d',
        CAST(
            substr(
                InvoiceDate,
                instr(InvoiceDate, '/') + 1,
                instr(
                    substr(InvoiceDate, instr(InvoiceDate, '/') + 1),
                    '/'
                ) - 1
            ) AS INTEGER
        )
    )
    || ' ' ||
    substr(
        InvoiceDate,
        instr(InvoiceDate, ' ') + 1
    );

    UPDATE customer_data_clean
SET InvoiceDateISO =
    substr(InvoiceDateISO, 1, 11)
    ||
    printf(
        '%02d',
        CAST(
            substr(
                InvoiceDateISO,
                12,
                instr(substr(InvoiceDateISO, 12), ':') - 1
            ) AS INTEGER
        )
    )
    ||
    substr(
        InvoiceDateISO,
        12 + instr(substr(InvoiceDateISO, 12), ':') - 1
    );

PRAGMA table_info(customer_data_clean);

SELECT COUNT(*) AS CleanedRows
FROM customer_data_clean;

SELECT
    InvoiceDate,
    InvoiceDateISO
FROM customer_data_clean
LIMIT 10;