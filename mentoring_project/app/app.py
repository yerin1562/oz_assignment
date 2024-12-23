from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

def get_news():
    connection = pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'user'),
        password=os.getenv('MYSQL_PASSWORD', 'password'),
        database=os.getenv('MYSQL_DB', 'naver_news'),
    )

    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM news")
    news = cursor.fetchall()
    connection.close()
    return news

@app.route("/news", methods=["GET"])
def news():
    return jsonify(get_news())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)