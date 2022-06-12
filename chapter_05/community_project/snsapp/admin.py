from django.contrib import admin
from .models import Post, Comment, IdComment, IdPost

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(IdPost)
admin.site.register(IdComment)
# Register your models here.
