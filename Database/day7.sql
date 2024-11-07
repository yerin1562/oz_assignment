USE fish_shaped_bun_shop;

SELECT * FROM fish_shaped_bun_shop.users;

INSERT INTO users(first_name, last_name, email, password, address, contact, is_active, is_staff, is_orderable)
VALUES ('Banana', 'Milk', 'isaid@justbanana.com', 'nomilk', 'bingre', '0101', 1, 1, 1);

UPDATE users SET address = 'notbingre'
WHERE id = 101;

INSERT INTO 
sales_records(
	user_id
)
VALUE(101);


INSERT INTO sales_items (
	sales_record_id, product_id, quantity
)
VALUES(
	51, 
    (SELECT id FROM products WHERE id=2), 3
);

INSERT INTO sales_items (
	sales_record_id, product_id, quantity
)
VALUES(
	51, 
    (SELECT id FROM products WHERE id=3), 2
);

INSERT INTO sales_items (
	sales_record_id, product_id, quantity
)
VALUES(
	51, 
    (SELECT id FROM products WHERE id=4), 5
);

INSERT INTO raw_materials(name, price)
VALUES ('Gangwon Corn', 10.00);


INSERT INTO order_records(user_id, raw_material_id, quantity)
VALUES(
(SELECT id FROM users WHERE id=101), 
(SELECT id FROM raw_materials WHERE id=15), 
1000
);

INSERT INTO order_records(user_id, raw_material_id, quantity)
VALUES(
(SELECT id FROM users WHERE id=101), 
(SELECT id FROM raw_materials WHERE id=14), 
165
);

INSERT INTO order_records(user_id, raw_material_id, quantity)
VALUES(
(SELECT id FROM users WHERE id=101), 
(SELECT id FROM raw_materials WHERE id=8), 
956
);

INSERT INTO daily_records(
stock_id, change_quantity, change_type
)
VALUES(
(SELECT id FROM stocks WHERE id=8),
956, 
'IN'
 );
 
 INSERT INTO stocks(
	raw_material_id, quantity
 )
 SELECT id, 1000 FROM raw_materials WHERE id=15;
 
 INSERT INTO daily_records(
stock_id, change_quantity, change_type
)
SELECT id, 165, 'IN' FROM stocks WHERE id=14
UNION ALL
SELECT id, 1000, 'IN' FROM stocks WHERE id=15;

-- UPDATE stocks s 
-- JOIN order_records o ON s.raw_material_id = o.raw_material_id
-- SET s.quantity = s.quantity + o.quantity;

SELECT 
sr.id AS sales_record_id, sr.created_at, 
u.first_name, u.last_name, 
si.product_id, 
SUM(si.quantity) AS total, 
p. price
FROM sales_items si
JOIN 
    sales_records sr ON si.sales_record_id = sr.id      -- 판매 항목과 판매 기록을 연결
JOIN 
    users u ON sr.user_id = u.id                        -- 판매 기록과 사용자를 연결
JOIN 
    products p ON si.product_id = p.id                 -- 판매 항목과 상품을 연결
WHERE 
    u.id = 11  -- 특정 유저 아이디 (여기서는 1번 유저로 설정)
GROUP BY 
    si.product_id, sr.id, sr.created_at, u.first_name, u.last_name, p.price
ORDER BY 
p.price DESC;



SELECT 
    sr.id AS sales_record_id,
    sr.created_at,
    u.first_name,
    u.last_name,
    si.product_id,
    SUM(si.quantity) AS total_quantity,
    p.price
FROM 
    sales_items si
JOIN 
    sales_records sr ON si.sales_record_id = sr.id      -- 판매 항목과 판매 기록을 연결
JOIN 
    users u ON sr.user_id = u.id                        -- 판매 기록과 사용자를 연결
JOIN 
    products p ON si.product_id = p.id                 -- 판매 항목과 상품을 연결
WHERE 
    u.id = 101  -- 특정 유저 아이디 
GROUP BY 
    si.product_id, sr.id, sr.created_at, u.first_name, u.last_name, p.price
ORDER BY 
    p.price DESC;                  -- 가격 기준으로 내림차순 정렬

