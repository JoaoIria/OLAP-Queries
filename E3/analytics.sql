-- Query 1: Quantity and total sales value of each product in 2022, globally, by city, month, day of the month, and day of the week
SELECT 
  SKU, 
  city, 
  month, 
  day_of_month, 
  day_of_week, 
  SUM(qty) AS total_qty, 
  SUM(total_price) AS total_sales_value
FROM 
  product_sales
WHERE 
  year = '2022'
GROUP BY 
  GROUPING SETS ((SKU, city, month, day_of_month, day_of_week), (SKU, month, day_of_month, day_of_week), (SKU, day_of_month, day_of_week), (SKU, day_of_week))
ORDER BY 
  SKU, city, month, day_of_month, day_of_week;

-- Query 2: Average daily sales value of all products in 2022, globally, by month and day of the week
SELECT 
  month, 
  day_of_week, 
  AVG(total_price) AS avg_daily_sales_value
FROM 
  product_sales
WHERE 
  year = '2022'
GROUP BY 
  ROLLUP (month, day_of_week)
ORDER BY 
  month, day_of_week;
