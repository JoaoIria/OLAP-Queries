-- QUERY 1
SELECT customer.cust_no, customer.name
FROM customer
JOIN pay ON customer.cust_no = pay.cust_no
GROUP BY customer.cust_no, customer.name
HAVING SUM(pay.order_no) = (
  SELECT MAX(total_orders)
  FROM (
    SELECT SUM(pay.order_no) AS total_orders
    FROM customer
    JOIN pay ON customer.cust_no = pay.cust_no
    GROUP BY customer.cust_no
  ) AS subquery
);

-- QUERY 2
SELECT employee.name
FROM employee
JOIN process ON employee.ssn = process.ssn
JOIN orders ON process.order_no = orders.order_no
WHERE EXTRACT(YEAR FROM orders.date) = 2022
GROUP BY employee.name
HAVING COUNT(DISTINCT orders.date) = (
  SELECT COUNT(DISTINCT orders.date)
  FROM orders
  WHERE EXTRACT(YEAR FROM orders.date) = 2022
);

-- QUERY 3
SELECT EXTRACT(MONTH FROM orders.date) AS month, COUNT(*) AS unpaid_orders
FROM orders
LEFT JOIN pay ON orders.order_no = pay.order_no
WHERE EXTRACT(YEAR FROM orders.date) = 2022 AND pay.order_no IS NULL
GROUP BY EXTRACT(MONTH FROM orders.date);