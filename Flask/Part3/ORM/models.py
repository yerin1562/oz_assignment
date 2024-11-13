# ModeL -> Table 생성 
# 게시글 - board 
# 유저 - user
from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(120),nullable=False)
    # 관계 맺기 / back_populates = 역참조
    # 테이블 내에서는 boards 보이지 않음 
    # lazy: 모든 데이터를 즉시 가져오는 것이 아니라, 필요할 때 해당 쿼리를 실행하여 데이터 로드
    boards = db.relationship('Board', back_populates='author', lazy='dynamic')

	# address = db.Column(db.String(120), unique=True, nullable=False)  # 추가된 필드

class Board(db.Model):
    __tablename__ = "boards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # 테이블 내에서는 author 보이지 않음 
    author = db.relationship('User', back_populates='boards')