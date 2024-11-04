import pymysql


# (1) db connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='yerin1562',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
    # cursorclass 의 기본값은 튜플 = 가장 단순하고 빠르기 때문 BUT json, 데이터 변경이 불가능함
)

# (2) CRUD - READ

# 1. SELECT * FROM

def get_customers():
    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers: ", customers['customerNumber']) 
    print("customers: ", customers['customerName']) 
    print("customers: ", customers['country']) 
    cursor.close()


# 2. INSERT INTO

def add_customer():
    cursor = connection.cursor()

    name = 'inseop'
    last_name = 'kim'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES (1000, '{name}', '{last_name}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# add_customer() 


# 3. UPDATE SET
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_inseop'
    contactLastName = 'update_kim'
    
    sql = "UPDATE customers SET customerName = %s, contactLastName = %s WHERE customerNumber = %s"
    cursor.execute(sql, (update_name, contactLastName, 1000))
    connection.commit()
    cursor.close()

# update_customer()


# 4. DELETE FROM

def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close() 

# delete_customer()
