-- Drop existing tables if they exist
DROP TABLE IF EXISTS Pay;
DROP TABLE IF EXISTS Delivery;
DROP TABLE IF EXISTS Supply_Contract;
DROP TABLE IF EXISTS Contains;
DROP TABLE IF EXISTS Process;
DROP TABLE IF EXISTS Works;
DROP TABLE IF EXISTS Places;
DROP TABLE IF EXISTS EAN_Product;
DROP TABLE IF EXISTS Warehouse;
DROP TABLE IF EXISTS Office;
DROP TABLE IF EXISTS Workplace;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Sale;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS "Order";
DROP TABLE IF EXISTS Supplier;

-- Create the tables

-- Customer table
CREATE TABLE Customer (
                          cust_no SERIAL PRIMARY KEY,
                          name VARCHAR(255) NOT NULL,
                          email VARCHAR(255) NOT NULL UNIQUE,
                          phone VARCHAR(20),
                          address VARCHAR(255)
);

-- Order table
CREATE TABLE "Order" (
                         order_no SERIAL PRIMARY KEY,
                         date DATE NOT NULL
);

-- Sale table
CREATE TABLE Sale (
                      order_no INT PRIMARY KEY,
                      FOREIGN KEY (order_no) REFERENCES "Order" (order_no)
);

-- Employee table
CREATE TABLE Employee (
                          ssn INT PRIMARY KEY,
                          TIN INT UNIQUE,
                          bdate DATE,
                          name VARCHAR(255)
);

-- Department table
CREATE TABLE Department (
    name VARCHAR(255) PRIMARY KEY
);

-- Workplace table
CREATE TABLE Workplace (
                           address VARCHAR(255) PRIMARY KEY,
                           lat DECIMAL(9, 6),
                           lon DECIMAL(9, 6),
                           UNIQUE (lat, lon)
);

-- Office table
CREATE TABLE Office (
                        address VARCHAR(255) PRIMARY KEY,
                        FOREIGN KEY (address) REFERENCES Workplace (address)
);

-- Warehouse table
CREATE TABLE Warehouse (
                           address VARCHAR(255) PRIMARY KEY,
                           FOREIGN KEY (address) REFERENCES Workplace (address)
);

-- Works table
CREATE TABLE Works (
    ssn INT,
    address VARCHAR(255),
    name VARCHAR(255),
    FOREIGN KEY (ssn) REFERENCES Employee (ssn),
    FOREIGN KEY (address) REFERENCES Workplace (address),
    FOREIGN KEY (name) REFERENCES Department (name),
    PRIMARY KEY (ssn, address, name)
);


-- Product table
CREATE TABLE Product (
                         sku SERIAL PRIMARY KEY,
                         name VARCHAR(255) NOT NULL,
                         description TEXT,
                         price DECIMAL(10, 2),
                         UNIQUE (sku)
);

-- EAN_Product table
CREATE TABLE EAN_Product (
                             sku INT,
                             EAN VARCHAR(255) PRIMARY KEY,
                             FOREIGN KEY (sku) REFERENCES Product (sku)
);

-- Supplier table
CREATE TABLE Supplier (
                          TIN INT PRIMARY KEY,
                          address VARCHAR(255),
                          name VARCHAR(255),
                          UNIQUE (TIN)
);

-- Pay table
CREATE TABLE Pay (
                     order_no INT,
                     cust_no INT,
                     FOREIGN KEY (order_no) REFERENCES "Order" (order_no),
                     FOREIGN KEY (cust_no) REFERENCES Customer (cust_no)
);

-- Places table
CREATE TABLE Places (
                        order_no INT,
                        cust_no INT,
                        FOREIGN KEY (order_no) REFERENCES "Order" (order_no),
                        FOREIGN KEY (cust_no) REFERENCES Customer (cust_no),
                        PRIMARY KEY (order_no, cust_no)
);

-- Process table
CREATE TABLE Process (
                         ssn INT,
                         order_no INT,
                         FOREIGN KEY (ssn) REFERENCES Employee (ssn),
                         FOREIGN KEY (order_no) REFERENCES "Order" (order_no),
                         PRIMARY KEY (ssn, order_no)
);

-- Contains table
CREATE TABLE Contains (
                          order_no INT,
                          sku INT,
                          qty INT,
                          FOREIGN KEY (order_no) REFERENCES "Order" (order_no),
                          FOREIGN KEY (sku) REFERENCES Product (sku),
                          PRIMARY KEY (order_no, sku)
);

-- Supply_Contract table
CREATE TABLE Supply_Contract (
                                 sku INT,
                                 TIN INT,
                                 Date DATE,
                                 FOREIGN KEY (sku) REFERENCES Product (sku),
                                 FOREIGN KEY (TIN) REFERENCES Supplier (TIN),
                                 PRIMARY KEY (sku, TIN)
);

-- Delivery table
CREATE TABLE Delivery (
                          address VARCHAR(255),
                          sku INT,
                          TIN INT,
                          FOREIGN KEY (address) REFERENCES Warehouse (address),
                          FOREIGN KEY (sku) REFERENCES Product (sku),
                          FOREIGN KEY (TIN) REFERENCES Supplier (TIN),
                          PRIMARY KEY (address, sku, TIN)
);

-- Add additional constraints

-- Constraint for Contains table
ALTER TABLE Contains ADD CONSTRAINT fk_Contains_order FOREIGN KEY (order_no) REFERENCES "Order" (order_no);

-- Constraint for Process table
ALTER TABLE Process ADD CONSTRAINT fk_Process_ssn FOREIGN KEY (ssn) REFERENCES Employee (ssn);
ALTER TABLE Process ADD CONSTRAINT fk_Process_order FOREIGN KEY (order_no) REFERENCES "Order" (order_no);

-- Constraint for Pay table
ALTER TABLE Pay ADD CONSTRAINT uk_Pay_order_cust UNIQUE (order_no, cust_no);
