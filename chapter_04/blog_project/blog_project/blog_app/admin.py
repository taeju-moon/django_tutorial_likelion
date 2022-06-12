from django.contrib import admin
from .models import Blog, Comment

#admin 사이트에서 내가 만든 models확인
admin.site.register(Blog)

admin.site.register(Comment)