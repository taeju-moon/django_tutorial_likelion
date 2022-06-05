from tkinter import CASCADE
from django.db import models

class Blog(models.Model):
    #django는 기본키를 자동으로 생성해줌
    #id = 숫자형
    title = models.CharField(max_length=200) #괄호 안에 제약사항 적어두기 가능
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #자동으로 지금 시간을 추가하겠다
    photo = models.ImageField(blank=True, upload_to='blog_photo') #선택사항임 / media 안에 blog_photo라는 폴더에 저장하겠음
    
    #admin페이지에서의 제목 설정을 title로 하겠다
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) #외래키, 게시물 삭제시 댓글도 삭제됨

    def __str__(self):
        return self.comment
        