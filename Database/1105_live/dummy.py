import pymysql
import random
from faker import Faker

# Faker 객체 생성
fake = Faker()

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='localhost',
    user='root',  # 사용자 이름
    password='yerin1562',  # 비밀번호
    database='fish_shaped_bun_shop',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


try:
    with connection.cursor() as cursor:
        # 더미 사용자 데이터 삽입
        for _ in range(50):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()
            password = fake.password()
            address = fake.address()
            contact = fake.phone_number()
            is_active = random.choice([True, False])
            is_staff = random.choice([True, False])
            is_orderable = random.choice([True, False])

            cursor.execute("""
                INSERT INTO users (first_name, last_name, email, password, address, contact, is_active, is_staff, is_orderable)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, email, password, address, contact, is_active, is_staff, is_orderable))

        # 더미 원재료 데이터 삽입
        raw_materials = [
            ('Flour', 1.76),
            ('Sugar', 2.00),
            ('Yeast', 0.50),
            ('Red Bean Paste', 4.50),
            ('Chocolate', 28.00),
            ('Cream', 4.50),
            ('Avocado', 11.40)
        ]
        for name, price in raw_materials:
            cursor.execute("""
                INSERT INTO raw_materials (name, price)
                VALUES (%s, %s)
            """, (name, price))

        # 더미 재고 데이터 삽입
        cursor.execute("SELECT id FROM raw_materials")
        raw_material_ids = [row['id'] for row in cursor.fetchall()]

        for raw_material_id in raw_material_ids:
            quantity = random.randint(50, 200)
            cursor.execute("""
                INSERT INTO stocks (raw_material_id, quantity)
                VALUES (%s, %s)
            """, (raw_material_id, quantity))

        for raw_material_id in raw_material_ids:
            for _ in range(20):
                last_updated = fake.date_time_this_year()  # 현재 연도 내의 날짜 및 시간 생성
                cursor.execute("""
                    INSERT INTO stocks
                    SET last_updated = %s
                    WHERE raw_material_id = %s
                """, (last_updated, raw_material_id))


        # 더미 제품 데이터 삽입
        products = [
            ('Fish Bun', 'A delicious fish-shaped bun.', 3.00),
            ('Red Bean Bun', 'Sweet bun filled with red bean paste.', 2.50),
            ('Chocolate Bun', 'Decadent chocolate-filled bun.', 3.50),
            ('Corn Bun', 'The greatest Gangwon corn bun.', 7.00) 
        ]
        for name, description, price in products:
            cursor.execute("""
                INSERT INTO products (name, description, price)
                VALUES (%s, %s, %s)
            """, (name, description, price))

        # 더미 판매 기록 데이터 삽입
        cursor.execute("SELECT id FROM users")
        user_ids = [row['id'] for row in cursor.fetchall()]
        cursor.execute("SELECT id FROM products")
        product_ids = [row['id'] for row in cursor.fetchall()]

        for user_id in user_ids:
            created_at = fake.date_time_this_year()
            cursor.execute("""
                INSERT INTO sales_records (user_id, created_at)
                VALUES (%s, %s)
            """, (user_id, created_at))

            sales_record_id = cursor.lastrowid
            for _ in range(random.randint(1, 3)):  # 1~3개의 상품을 추가
                product_id = random.choice(product_ids)
                quantity = random.randint(1, 5)
                cursor.execute("""
                    INSERT INTO sales_items (sales_record_id, product_id, quantity)
                    VALUES (%s, %s, %s)
                """, (sales_record_id, product_id, quantity))

        # daily records 테이블에 더미 데이터 20개 만들기
        cursor.execute("SELECT id FROM stocks")
        stock_ids = [row['id'] for row in cursor.fetchall()]
        
        for _ in range(20):
            stock_id = random.choice(stock_ids)
            change_quantity = random.randint(-50, 50)  # 음수와 양수를 섞어서 수량 변화값 생성
            change_type = random.choice(['IN', 'OUT', 'RETURNED', 'DISCARDED']) 
            
            # 데이터 삽입
            cursor.execute(""" 
                INSERT INTO daily_records (stock_id, change_quantity, change_type)
                VALUES (%s, %s, %s)
            """, (stock_id, change_quantity, change_type))

        # 변경 사항 커밋
        connection.commit()
finally:
    connection.close()


# # 과제
# - stocks 테이블에 더미 데이터 20개 이상 만들기 O 
# - daily_records 테이블의에 더미 데이터 20개 만들기
# - products 테이블에 데이터를 insert 시 본인만의 시그니쳐 메뉴 포함해서 넣기 