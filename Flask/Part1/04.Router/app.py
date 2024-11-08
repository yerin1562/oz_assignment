from flask import Flask, request, Response

app = Flask(__name__) 

@app.route('/')
def home():
    return "Hello, This is Main Page!"

@app.route('/about')
def about():
    return "Hello, This is the About Page!"


# 동적 파라미터 값을 받아줌
#http://127.0.0.1:5000/user/yerin
@app.route('/user/<username>')
def user_profile(username):
    return f'Username : {username}'

# URL에 변수 및 타입 지정
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post ID: {post_id}'

#post 요청 날리는 법
# (1) postman
# (2) request
import requests

@app.route('/test')
def test():
    url = "http://127.0.0.1:5000/submit"
    response = requests.post(url = url, data = data)

    return response

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        return 'POST method.'
    else:
        return 'GET method.'


if __name__ == "__main__":
    app.run()


# python -m flask 
    # (on terminal) options in flask modules
    
# flask run
# flask --app app.py --debug run
    # (on terminal) run

# flask --help
