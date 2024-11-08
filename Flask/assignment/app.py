from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    users = [
    {"username": "GOD", "name": "Farmer"},
    {"username": "Beer Queen", "name": "Suhyun"},
    {"username": "SangMen", "name": "SangHun"},
    {"username": "DB Queen", "name": "Yerin"},
    {"username": "MangGom", "name": "JungJe"},
    {"username": "Hyochori", "name": "HyoJong"},
    {"username": "lawyer", "name": "Mir"},
    {"username": "Autumn", "name": "GaEul"},
    {"username": "Computer Scientist", "name": "Yejin"},
    {"username": "BombiMom", "name": "Solbi"},
    {"username": "Security expert", "name": "Kiyeon"},
    {"username": "Health Trainer", "name": "Dongok"},
    {"username": "Shy Boy", "name": "Bakgeol"},
    {"username": "Hard Worker", "name": "Hyoeun"},
    {"username": "GOAT", "name": "HongMin"}
]
    return render_template('index.html', users = users)

if __name__ == "__main__":
    app.run(debug = True)
