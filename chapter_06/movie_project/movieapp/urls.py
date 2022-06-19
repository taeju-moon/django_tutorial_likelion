from distutils.file_util import move_file
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<str:movie_id>', views.detail, name="detail"),
]