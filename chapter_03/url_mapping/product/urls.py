from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.productlist),
    path('/first', views.productfirst),
]