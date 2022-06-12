from django.db import models
from django.contrib.auth.models import User

# 게시글 모델(익명게시판)
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 댓글 모델(익명게시판)
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, db_column="post_id")

    def __str__(self):
        return self.comment

# 게시글 모델(실명게시판)
class IdPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 댓글 모델(실명게시판)
class IdComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(IdPost, null=True, on_delete=models.CASCADE, db_column="post_id")

    def __str__(self):
        return self.comment