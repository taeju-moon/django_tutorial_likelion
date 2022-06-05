from django.contrib import admin
from django.urls import path, include
from board import views

urlpatterns = [
    path('', views.board),
    path('/first', views.boardfirst)
]