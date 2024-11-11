# Marshmellow 모듈로 데이터 타입 바꾸기
from marshmallow import Schema, fields


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)