# API list
#/board/
# 전체 게시글 불러오기 (GET)
# 게시물 작성(POST)

from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# API list
#/board/
# 전체 게시글 불러오기 (GET)
# 게시물 작성(POST)

@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        return jsonify([{"user_id": board.user_id, 
                        "id": board.id,
                        "title": board.title, "content": board.content, "author": board.author.name} for board in boards])

            # for board in boards:
            #print('id', board. id)
            #print('title', board.title)
            #print ('content', board. content)
            #print ('user_id', board.user_id)
            #print('author_name', board. author. name) # User
            #print('author_email', board.author.email) # User

    def post(self):
        data = request.json
        new_board = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_board)
        db.session.commit()
        return jsonify({"message": "Board created"}), 201

# /board/<int:board_id>
# 하나의 게시글 불러오기 (GET)
# 특정 게시글 수정하기 (PUT)
# 특정 게시글 삭제하기(DELETE)

@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return jsonify({"title": board.title, "content": board.content, "author": board.author.name})

    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        return jsonify({"message": "Board updated"})

    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()
        return jsonify({"message": "Board deleted"})