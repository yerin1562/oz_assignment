import requests 
from bs4 import BeautifulSoup
# 정적 크롤링

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=%"
keyword = input("검색을 원하는 키워드를 입력해주세요")

header_user = {"User-Agent" : 
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

url = base_url + keyword
req = requests.get(url, headers = header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

results = soup.select(".view_wrap") # 결과물은 리스트 형태의 자료형

for i in results:
    title = i.select_one(".title_link").text
    write = i.select_one(".name").text
    link = i.select_one(".title_link")["href"]
    if i.select_one(".dsc_area"):
        dsc = i.select_one(".dsc_area").text
    else: 
        dsc = "내용없음"
    print(f'제목: {title}')
    print(f'작성자 : {write}')
    print(f'링크 : {link}')
    print(f'요약 : {dsc}')
    print("----------------------------------------")



# 광고 제거
# .spblog ico_ad