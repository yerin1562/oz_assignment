from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'title': 'Flask Jinja Template',
        'user': 'yerin',
        'is_admin': True, 
        'item_list': ["Item1","Item2", "Item3"]
    }


# (1) rendering 할 html 파일명 입력
# (2) html 로 넘겨줄 데이터 입력
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(debug = True)
    # debug 를 키면 코드를 변경하면 실시간으로 반영해줌