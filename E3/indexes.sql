CREATE INDEX idx_product_price ON product(price);

CREATE INDEX idx_orders_order_no_date ON orders(order_no, date);

CREATE INDEX idx_product_SKU ON product(SKU);


###########################
An index on the price field in the product table. This index will make the price > 50 condition in your WHERE clause faster because the database will be able to find the products with a price greater than 50 without scanning the entire table.

A composite index on the order_no and date fields in the orders table. This index will help speed up the join operation with the contains table as well as the date comparison in the WHERE clause.

An index on the SKU field in the product table. This will speed up the join operation with the contains table.

//
CREATE INDEX idx_product_price ON product(price); - This is a single-column B-tree index on the price column of the product table. In a B-tree index, the values are stored in order, which allows for fast lookup of individual values and efficient access to a range of values. This makes it suitable for the price > 50 condition in the query.

CREATE INDEX idx_orders_order_no_date ON orders(order_no, date); - This is a multi-column (also known as composite) B-tree index on the order_no and date columns of the orders table. A composite index is used when queries often filter by two or more specific columns. The order of columns in the index definition matters. The index is most effective when the query conditions use the indexed columns in the order they are defined in the index.

CREATE INDEX idx_product_SKU ON product(SKU); - This is a single-column B-tree index on the SKU column of the product table.
##################


CREATE INDEX idx_product_name ON product(name);

CREATE INDEX idx_contains_SKU ON contains(SKU);

CREATE INDEX idx_product_SKU ON product(SKU);


#############################

An index on the name field in the product table. This index will make the name LIKE 'A%' condition in your WHERE clause faster because the database will be able to find the products with names starting with 'A' without scanning the entire table.

A composite index on the SKU field in both the contains and product tables. This index will help speed up the join operation.

//
The idx_product_SKU index might already exist if you created it for the previous query.

These are all B-tree indexes. The idx_product_name index is particularly useful for the LIKE 'A%' condition because B-tree indexes can efficiently handle prefix queries, which is a query where you're looking for all values that start with a certain string.



/// PARA O AMADEU
-> olhar só para as justificações dos indexes e tentar perceber/elaborar (parece-me q eles demoraram 2h a aprender a matéria e n a fazer)
-> report (anyhting)