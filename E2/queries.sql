
-- 1 --

SELECT DISTINCT c.name
FROM customer c
         JOIN places pl ON c.cust_no = pl.cust_no
         JOIN "Order" o ON pl.order_no = o.order_no
         JOIN contains cn ON o.order_no = cn.order_no
         JOIN product p ON cn.sku = p.sku
WHERE p.price > 50
  AND EXTRACT(YEAR FROM o.date) = 2023;

-- 2 --

SELECT DISTINCT e.name
FROM employee e
         JOIN works w ON e.ssn = w.ssn
         JOIN workplace wp ON w.address = wp.address
         JOIN warehouse wh ON wh.address = wp.address
         LEFT JOIN office o ON o.address = wp.address
         JOIN process pr ON e.ssn = pr.ssn
         JOIN "Order" ord ON pr.order_no = ord.order_no
WHERE EXTRACT(MONTH FROM ord.date) = 1
  AND EXTRACT(YEAR FROM ord.date) = 2023
  AND o.address IS NULL;

-- 3 --

SELECT p.name
FROM product p
         JOIN contains cn ON p.sku = cn.sku
GROUP BY p.name
ORDER BY SUM(cn.qty) DESC
LIMIT 1;


-- 4 --

SELECT o.order_no, SUM(p.price * cn.qty) AS total_value
FROM "Order" o
         JOIN contains cn ON o.order_no = cn.order_no
         JOIN product p ON cn.sku = p.sku
GROUP BY o.order_no
ORDER BY o.order_no;
