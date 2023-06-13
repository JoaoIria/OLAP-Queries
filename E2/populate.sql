-- Remove existing records from the tables
DELETE FROM Pay;
DELETE FROM Process;
DELETE FROM Delivery;
DELETE FROM Supply_Contract;
DELETE FROM Contains;
DELETE FROM Works;
DELETE FROM Places;
DELETE FROM EAN_Product;
DELETE FROM Warehouse;
DELETE FROM Office;
DELETE FROM Workplace;
DELETE FROM Department;
DELETE FROM Employee;
DELETE FROM Sale;
DELETE FROM Customer;
DELETE FROM Product;
DELETE FROM "Order";
DELETE FROM Supplier;

-- Insert data into the "customer" table
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (1, 'Costumer1', 'costumer1@example.com', '123456789', 'Lisboa');
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (2, 'Costumer2', 'costumer2@example.com', '111222333', 'Porto');
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (3, 'Numero8dig', 'Numero8dig@example.com', '11122233', 'Porto');
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (4, 'NumerocLetras', 'umerocLetras@example.com', 'ABC123123', 'Porto');
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (5, 'NomCidadeGigante', 'NomCidadeGigante@example.com', '11122233', 'Pneumoultramicroscopicossilicovulcanoconiótico');
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (6, 'NomCicacdeEspacos', 'NomCicacdeEspacos@example.com', '111222333', 'Porto Salvo');
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES (7, 'NumAdrNULL', 'NumAdrNULL@example.com', NULL, NULL);

-- Insert data into the "Order" table
INSERT INTO "Order" (order_no, date)
VALUES (1, '2023-01-01');
INSERT INTO "Order" (order_no, date)
VALUES (2, '2023-01-25');
INSERT INTO "Order" (order_no, date)
VALUES (3, '1800-05-25');
INSERT INTO "Order" (order_no, date)
VALUES (4, '2023-02-25');
INSERT INTO "Order" (order_no, date)
VALUES (5, '2023-07-25');

-- Insert data into the "Sale" table
INSERT INTO Sale (order_no)
VALUES (1);
INSERT INTO Sale (order_no)
VALUES (2);
INSERT INTO Sale (order_no)
VALUES (3);
INSERT INTO Sale (order_no)
VALUES (4);
INSERT INTO Sale (order_no)
VALUES (5);

-- Insert data into the "Employee" table
INSERT INTO Employee (ssn, tin, bdate, name)
VALUES (123456789, 987654321, '1999-01-10', 'Employee1');
INSERT INTO Employee (ssn, tin, bdate, name)
VALUES (987654321, 123456789, '1999-01-10', 'Employee2');
INSERT INTO Employee (ssn, tin, bdate, name)
VALUES (9823948, 283649753, '1999-01-10', 'SSN7dig');
INSERT INTO Employee (ssn, tin, bdate, name)
VALUES (982394987, 927497367, '1600-01-10', 'Oldbdate');
INSERT INTO Employee (ssn, tin, bdate, name)
VALUES (987654322, 123496789, '1999-01-10', 'Nome com espaco');

-- Insert data into the "Supplier" table
INSERT INTO Supplier (tin, address, name)
VALUES (111111111, 'Supplier Address', 'Supplier Name');
INSERT INTO Supplier (tin, address, name)
VALUES (222222222, 'Supplier Address 2', 'Supplier Name 2');
INSERT INTO Supplier (tin, address, name)
VALUES (33333333, 'Supplier Address 3', 'tin8dig');

-- Insert data into the "Department" table
INSERT INTO Department (name)
VALUES ('IT');
INSERT INTO Department (name)
VALUES ('Nome Com Espaco');

-- Insert data into the "Workplace" table
INSERT INTO Workplace (address, lat, lon)
VALUES ('Aveiro', 40.6412, -8.65362);
INSERT INTO Workplace (address, lat, lon)
VALUES ('Lisboa', 38.7071, -9.13549);
INSERT INTO Workplace (address, lat, lon)
VALUES ('Porto', 41.15, -8.61024);
INSERT INTO Workplace (address, lat, lon)
VALUES ('Adress Com Espaco', 49.6412, -8.65382);

-- Insert data into the "Office" table
INSERT INTO Office (address)
VALUES ('Aveiro');
INSERT INTO Office (address)
VALUES ('Lisboa');
INSERT INTO Office (address)
VALUES ('Adress Com Espaco');

-- Insert data into the "Warehouse" table
INSERT INTO Warehouse (address)
VALUES ('Aveiro');
INSERT INTO Warehouse (address)
VALUES ('Porto');
INSERT INTO Warehouse (address)
VALUES ('Adress Com Espaco');

-- Insert data into the "Product" table
INSERT INTO Product (sku, name, description, price)
VALUES (1, 'Product 1', 'Description 1', 10.99);
INSERT INTO Product (sku, name, description, price)
VALUES (2, 'Product 2', 'Description 2', 60.99);
INSERT INTO Product (sku, name, description, price)
VALUES (3, 'Product 3', 'Description 3', 99.99);
INSERT INTO Product (sku, name, description, price)
VALUES (4, 'Product 4', 'Description 4', 98.99);

-- Insert data into the "EAN_Product" table
INSERT INTO EAN_Product (sku, EAN)
VALUES (1, 'EAN123');
INSERT INTO EAN_Product (sku, EAN)
VALUES (2, 'EAN Com Espaco');

-- Insert data into the "Contains" table
INSERT INTO Contains (order_no, sku, qty)
VALUES (1, 1, 1);
INSERT INTO Contains (order_no, sku, qty)
VALUES (1, 2, 1);
INSERT INTO Contains (order_no, sku, qty)
VALUES (2, 3, 1);
INSERT INTO Contains (order_no, sku, qty)
VALUES (3, 4, 1);
INSERT INTO Contains (order_no, sku, qty)
VALUES (4, 4, 1);
INSERT INTO Contains (order_no, sku, qty)
VALUES (5, 1, 10);

-- Insert data into the "Supply_Contract" table
INSERT INTO Supply_Contract (sku, tin, date)
VALUES (1, 111111111, '2025-01-01');
INSERT INTO Supply_Contract (sku, tin, date)
VALUES (3, 222222222, '2025-01-01');
INSERT INTO Supply_Contract (sku, tin, date)
VALUES (4, 33333333, '1900-01-01');

-- Insert data into the "Delivery" table
INSERT INTO Delivery (address, sku, tin)
VALUES ('Aveiro', 1, 111111111);
INSERT INTO Delivery (address, sku, tin)
VALUES ('Adress Com Espaco', 2, 222222222);

-- Insert data into the "Pay" table
INSERT INTO Pay (cust_no, order_no)
VALUES (1, 1);
INSERT INTO Pay (cust_no, order_no)
VALUES (1, 2);
INSERT INTO Pay (cust_no, order_no)
VALUES (4, 4);
INSERT INTO Pay (cust_no, order_no)
VALUES (3, 3);
INSERT INTO Pay (cust_no, order_no)
VALUES (5, 5);

-- Insert data into the "Places" table
INSERT INTO Places (cust_no, order_no)
VALUES (1, 1);
INSERT INTO Places (cust_no, order_no)
VALUES (2, 2);
INSERT INTO Places (cust_no, order_no)
VALUES (3, 3);
INSERT INTO Places (cust_no, order_no)
VALUES (4, 4);
INSERT INTO Places (cust_no, order_no)
VALUES (5, 5);

-- Insert data into the "Process" table
INSERT INTO Process (ssn, order_no)
VALUES (123456789, 2);

-- Insert data into the "Works" table
INSERT INTO Works (ssn, address, name)
VALUES (123456789, 'Porto', 'IT');
INSERT INTO Works (ssn, address, name)
VALUES (987654321, 'Aveiro', 'IT');
INSERT INTO Works (ssn, address, name)
VALUES (9823948, 'Adress Com Espaco', 'Nome Com Espaco');