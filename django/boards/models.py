from django.db import models

# 게시글
# - title
# - content

class Board(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()