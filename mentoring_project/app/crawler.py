import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pymysql
import os

def parse_relative_time(relative_time):
    now = datetime.now()
    if '분' in relative_time:
        return now - timedelta(minutes=int(relative_time.replace('분 전', '').strip()))
    elif '시간' in relative_time:
        return now - timedelta(hours=int(relative_time.replace('시간 전', '').strip()))
    elif '일' in relative_time:
        return now - timedelta(days=int(relative_time.replace('일 전', '').strip()))
    return now

def crawl_news():
    url = "https://news.naver.com/breakingnews/section/105/283"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.select(".list_body .list_title"):
        title = item.text.strip()
        description = "요약 없음"
        time_text = "1시간 전"  # Replace with actual selector.
        created_at = parse_relative_time(time_text)

        news_items.append((title, description, created_at))

    return news_items

def save_to_db(news_items):
    connection = pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'user'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DB', 'naver_news'),
    )

    cursor = connection.cursor()
    for title, description, created_at in news_items:
        cursor.execute(
            "INSERT INTO news (title, description, created_at) VALUES (%s, %s, %s)",
            (title, description, created_at),
        )
    connection.commit()
    connection.close()

if __name__ == "__main__":
    news = crawl_news()
    save_to_db(news)