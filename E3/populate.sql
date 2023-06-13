-- Populate customer table
INSERT INTO customer (cust_no, name, email, phone, address)
VALUES
  (1, 'John Doe', 'johndoe@example.com', '123456789', 'Rua Alegria, 123'),
  (2, 'Jane Smith', 'janesmith@example.com', '987654321', 'Rua do Carmo, 456'),
  (3, 'David Silva', 'davidsilva@example.com', '111222333', 'Avenida da Liberdade, 789'),
  (4, 'Maria Santos', 'mariasantos@example.com', '444555666', 'Rua Garrett, 10'),
  (5, 'Paulo Costa', 'paulocosta@example.com', '777888999', 'Praça do Comércio, 15');

-- Populate employee table
INSERT INTO employee (ssn, TIN, bdate, name)
VALUES
  ('123456789', '987654321', '1990-05-15', 'John Smith'),
  ('987654321', '123456789', '1985-12-03', 'Anna Johnson'),
  ('111222333', '444555666', '1992-08-20', 'Pedro Oliveira'),
  ('444555666', '111222333', '1988-04-10', 'Marta Almeida'),
  ('777888999', '555666777', '1995-11-01', 'Carlos Pereira');


-- Populate product table
INSERT INTO product (SKU, name, description, price, ean)
VALUES
  ('12345', 'Product A', 'Description of Product A', 9.99, 1234567890123),
  ('23456', 'Product B', 'Description of Product B', 19.99, 2345678901234),
  ('34567', 'Product C', 'Description of Product C', 29.99, 3456789012345),
  ('45678', 'Product D', 'Description of Product D', 39.99, 4567890123456),
  ('56789', 'Product E', 'Description of Product E', 49.99, 5678901234567);



START TRANSACTION;
SET CONSTRAINTS ALL DEFERRED;
-- Populate orders table
INSERT INTO orders (order_no, cust_no, date)
VALUES
    (1, 1, '2022-01-10'),
    (2, 2, '2022-01-10'),
    (3, 3, '2022-01-10'),
    (4, 4, '2022-01-10'),
    (5, 5, '2022-01-10');
-- Populate contains table
INSERT INTO contains (order_no, SKU, qty)
VALUES
    (1, '12345', 2),
    (2, '23456', 1),
    (3, '34567', 3),
    (4, '45678', 2),
    (5, '56789', 4);
COMMIT;

-- Populate process table
INSERT INTO process (ssn, order_no)
VALUES
  ('123456789', 1),
  ('987654321', 2),
  ('111222333', 3),
  ('444555666', 4),
  ('777888999', 5);

-- Populate department table
INSERT INTO department (name)
VALUES
  ('Sales'),
  ('Marketing'),
  ('Finance'),
  ('Human Resources'),
  ('IT');

-- Populate workplace table
INSERT INTO workplace (address, lat, long)
VALUES
  ('Rua Augusta, 123', 38.712345, -9.132456),
  ('Avenida Paulista, 456', -23.567890, -46.789012),
  ('Praça da República, 789', 41.987654, -8.123456),
  ('Rua dos Aliados, 10', 41.123456, -8.987654),
  ('Avenida da Boavista, 15', 41.654321, -8.567890);

-- Populate office table
INSERT INTO office (address)
VALUES
  ('Rua dos Aliados, 10'),
  ('Avenida da Boavista, 15');

-- Populate warehouse table
INSERT INTO warehouse (address)
VALUES
  ('Rua Augusta, 123'),
  ('Avenida Paulista, 456'),
  ('Praça da República, 789');

-- Populate works table
INSERT INTO works (ssn, name, address)
VALUES
  ('123456789', 'Sales', 'Rua Augusta, 123'),
  ('987654321', 'Marketing', 'Avenida Paulista, 456'),
  ('111222333', 'Finance', 'Praça da República, 789'),
  ('444555666', 'Human Resources', 'Rua dos Aliados, 10'),
  ('777888999', 'IT', 'Avenida da Boavista, 15');


-- Populate pay table
INSERT INTO pay (order_no, cust_no)
VALUES
  (1, 1),
  (2, 2),
  (3, 3);

-- Populate supplier table
INSERT INTO supplier (TIN, name, address, SKU, date)
VALUES
  ('987654321', 'Supplier A', 'Rua das Flores, 123', '12345', '2023-01-05'),
  ('123456789', 'Supplier B', 'Avenida dos Aliados, 456', '23456', '2023-02-10'),
  ('444555666', 'Supplier C', 'Praça do Comércio, 789', '34567', '2023-03-15'),
  ('111222333', 'Supplier D', 'Rua do Carmo, 10', '45678', '2023-04-20'),
  ('777888999', 'Supplier E', 'Avenida da Liberdade, 15', '56789', '2023-05-25');

-- Populate delivery table
INSERT INTO delivery (address, TIN)
VALUES
  ('Rua Augusta, 123', '987654321'),
  ('Avenida Paulista, 456', '123456789'),
  ('Praça da República, 789', '444555666');