CREATE INDEX idx_product_price ON product(price);

CREATE INDEX idx_orders_order_no_date ON orders(order_no, date);

CREATE INDEX idx_product_SKU ON product(SKU);



CREATE INDEX idx_product_name ON product(name);

CREATE INDEX idx_contains_SKU ON contains(SKU);