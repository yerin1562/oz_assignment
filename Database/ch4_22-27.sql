USE classicmodels;

-- 직원 추가
INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)
VALUES (501, 'Gwak', 'Yerin', 'x9999', 'yerin@example.com', '1', NULL, 'Backend Developer');

-- 사무실 추가
INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory)
VALUES ('1', 'New City', '555-5678', '456 Second St', NULL, 'NY', 'Country X', '12345', 'Territory');

-- 고객 추가 (customerNumber는 500으로 설정)
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (500, 'New Customer', 'Doe', 'John', '555-1234', '123 Main St', NULL, 'New City', 'NY', '10001', 'Country X', 500, 50000.00);

-- 제품 추가
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES ('P1234', 'New Product', 'Product Line A', '1:10', 'Vendor A', 'Description for new product', 50, 20.00, 25.00);

-- 주문 추가 (customerNumber는 500으로 설정)
INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)
VALUES (500, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), NULL, 'In Progress', 'New Order', 500);

-- 주문 상세 추가 (productCode는 P1234로 설정)
INSERT INTO orderdetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)
VALUES (500, 'P1234', 10, 20.00, 1);

-- 결제 추가 (customerNumber는 500으로 설정)
INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount)
VALUES (500, 'CHK9999', CURDATE(), 200.00);

-- 제품 라인 추가
INSERT INTO productlines (productLine, textDescription, htmlDescription, image)
VALUES ('New Product Line', 'Description for new product line', '<p>HTML description for new product line</p>', NULL);

-- 다른 고객 추가 (customerNumber는 501로 설정)
INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)
VALUES (501, 'Another Customer', 'Lee', 'Soo', '555-9876', '789 Third St', NULL, 'Another City', 'CA', '90001', 'Country Y', 500, 30000.00);

-- 다른 제품 추가
INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)
VALUES ('P5678', 'Another Product', 'Product Line B', '1:5', 'Vendor B', 'Description for another product', 30, 35.00, 45.00);

SELECT * FROM customers;

SELECT * FROM products;

SELECT firstName, lastName, jobTitle FROM employees;

SELECT city, state, country FROM offices;

SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;

SELECT * FROM orderdetails WHERE orderNumber = 501;

SELECT * FROM payments WHERE customerNumber = 502;

SELECT productLine, textDescription FROM productlines;

SELECT * FROM customers WHERE city = 'New City';

SELECT * FROM products WHERE buyPrice BETWEEN 20 AND 30;

UPDATE customers 
SET addressLine1 = '새로운 주소' 
WHERE customerNumber = 502;

UPDATE products 
SET buyPrice = 25.00 
WHERE productCode = 'P1234';

UPDATE employees 
SET jobTitle = 'Senior Sales Manager' 
WHERE employeeNumber = 501;

UPDATE offices 
SET phone = '555-6789' 
WHERE officeCode = '1';

UPDATE orders 
SET status = 'Shipped' 
WHERE orderNumber = 501;

UPDATE orderdetails 
SET quantityOrdered = 15 
WHERE orderNumber = 501 AND productCode = 'P1234';

UPDATE payments 
SET amount = 250.00 
WHERE customerNumber = 502 AND checkNumber = 'CHK9999';

UPDATE productlines 
SET textDescription = '업데이트된 제품 라인 설명' 
WHERE productLine = 'New Product Line';

UPDATE customers 
SET email = 'new.email@example.com' 
WHERE customerNumber = 502;

UPDATE products 
SET buyPrice = 30.00 
WHERE productCode IN ('P1234', 'P5678');


DELETE FROM customers 
WHERE customerNumber = 502;

DELETE FROM products 
WHERE productCode = 'P1234';

DELETE FROM employees 
WHERE employeeNumber = 501;

DELETE FROM offices 
WHERE officeCode = '1';

DELETE FROM orders 
WHERE orderNumber = 501;

DELETE FROM orderdetails 
WHERE orderNumber = 501 AND productCode = 'P1234';

DELETE FROM payments 
WHERE customerNumber = 502 AND checkNumber = 'CHK9999';

DELETE FROM productlines 
WHERE productLine = 'Old Product Line';

DELETE FROM customers 
WHERE city = 'Old City';

DELETE FROM products 
WHERE productLine = 'Discontinued Products';



