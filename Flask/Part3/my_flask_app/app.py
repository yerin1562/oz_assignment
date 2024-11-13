from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
# yaml: 데이터 직렬화 양식/ Yet Another Maekup Language
import yaml
from posts_routes import create_posts_blueprint

app = Flask(__name__)

# db 초기 설정

db = yaml.load(open('/Users/mac/Desktop/oz_assignment/Flask/Part3/my_flask_app/db.yaml'), Loader=yaml.FullLoader)
app.config["MYSQL_HOST"] = db['mysql_host']
app.config["MYSQL_USER"] = db['mysql_user']
app.config["MYSQL_PASSWORD"] = db['mysql_password']
app.config["MYSQL_DB"] = db['mysql_db']

mysql = MySQL(app)

# blueprint 설정
app.config['API_TITLE'] = 'Blog API List'
app.config['API_VERSION'] = '1.0'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWQGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
posts_blp = create_posts_blueprint(mysql)
api.register_blueprint(posts_blp)

# html route 설정 / 보기
from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template("posts.html")

# 실행 with debug
if __name__ == "__main__":
    app.run(debug=True)