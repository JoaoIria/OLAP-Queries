-- Drop the product_sales view if it already exists
DROP VIEW IF EXISTS product_sales;

-- Create the product_sales view
CREATE VIEW product_sales AS
SELECT
  c.SKU,
  TO_CHAR(o.date, 'Day') AS day_of_week,
  REGEXP_REPLACE(cust.address, '.*([0-9]{4}-[0-9]{3}) ([A-Za-zÀ-ÿ -]+)$', '\2') AS city,
  c.order_no,
  c.qty,
  c.qty * p.price AS total_price,
  TO_CHAR(o.date, 'YYYY') AS year,
  TO_CHAR(o.date, 'Month') AS month,
  EXTRACT(DAY FROM o.date) AS day_of_month
FROM
  contains c
JOIN
  pay pa ON c.order_no = pa.order_no
JOIN
  product p ON c.SKU = p.SKU
JOIN
  orders o ON c.order_no = o.order_no
JOIN
  customer cust ON o.cust_no = cust.cust_no;

-- Query the product_sales view
SELECT * FROM product_sales;
