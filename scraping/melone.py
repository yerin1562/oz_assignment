# 멜론 차트 top 100
# 순위, 제목, 가수, 앨범
# header_user 필수

import requests 
from bs4 import BeautifulSoup
# 정적 크롤링

header_user = {"User-Agent" : 
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}


url = "https://www.melon.com/chart/index.htm"
req = requests.get(url, headers=header_user)


html = req.text
soup = BeautifulSoup(html, "html.parser")

lst50 = soup.select(".lst50") # 리스트와 동일한 형태 인덱스 보유
lst100 = soup.select(".lst100") # 리스트와 리스트를 합치면 (+)

top100 = lst50 + lst100


# 순위 (rank)
# 제목  ellipsis rank01
# 가수 (text)  ellipsis rank02
# 앨범 (text)  ellipsis rank03

for rank, i in enumerate(top100, 1):
    title = i.select_one(".ellipsis.rank01 a").text
    artist = i.select_one(".ellipsis.rank02 a").text
    album = i.select_one(".ellipsis.rank03 a").text

    print(f'[순위]: {rank}')
    print(f'[제목]: {title}')
    print(f'[가수] : {artist}')
    print(f'[앨범] : {album}')
    print("----------------------------------------")

