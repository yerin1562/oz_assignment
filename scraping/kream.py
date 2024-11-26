from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
#클래스, 아디를 CSS_SELECTOR 이용하기 위한 패키지
from selenium.webdriver.common.by import By
# 키보드의 입력 형태를 코드로 작성하기 위한 패키지
from selenium.webdriver.common.keys import Keys

import time
import pymysql

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


options_ = Options()
options_.add_argument(f"User_Agent={header_user}")
# 크롬 창이 종료되지 않는 코드
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options_)

url = "https://kream.co.kr"

keyword = input("검색을 원하는 키워드를 입력해주세요")

driver.get(url)
time.sleep(2)

# driver ==> chrom browser
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(2)


driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(keyword)
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

for i in range(20):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card") # 리스ㅌ ㅡ가능한 데이터 타입

product_list = []

for item in items:
    '''
    제품명에 "후드"가 들어간 것만 추출 / 
    1. 제품명만 추출합니다. 
    2. 제픔명을 if 문을 이용해서 분류
    3. 문자열 안에 "후드"가 있는지 조건문을 만든다.
    '''
    product_name = item.select_one(".translated_name").text
    if "후드" in product_name:
        category = "상의"
        product_brand = item.select_one(".product_info_brand.brand").text
        product_price = item.select_one(".amount").text
        
        product = [category, product_brand, product_name, product_price]
        product_list.append(product) # [[상의, 슈프림, 멜란지 후드, 50000], ...]

        print(f"카테고리 : {category}")
        print(f"브랜드 : {product_brand}")
        print(f"제품명 : {product_name}")
        print(f"가격 : {product_price}")

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root', 
    password = 'yerin1562',
    db = 'kream',
    charset = 'utf8mb4'
)

# connection.cursor() # mysql 에 데이터를 넣거나 가져오거나 쿼리문을 실행 등 여러가지 역학을 해주는 객체 

def execute_query(connection, query, args = None): # args('jhon', '25', 'california')
    with connection.cursor() as cursor: 
        cursor.execute(query, args or ()) # 쿼리문을 담아서 데이터베이스 보냄 / select 검색 결과가 나올것이고 / inser 데이터베이스 데이터가 저장
        if query.strip().upper().startswith('SELECT'): # SELECT * from kream or insert
            return cursor.fetchall()
        else: 
            connection.commit() # 데이터베이스에 insert문을 사용했다면 데이터베이스에 데이터를 영구적으로 저장해줘

for i in product_list:  # [[상의, 슈프림, 후드, 54000], [...]...]
    # [[상의, 슈프림, 후드, 54000]
    execute_query(connection, "INSERT INTO kream (category, brand, product_name, price) VALUES (%s, %s, %s, %s)", (i[0], i[1], i[2], i[3]))

