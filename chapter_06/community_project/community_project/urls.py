"""community_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from snsapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),
    path('postcreate', views.postcreate, name="postcreate"),
    path('detail/<int:post_id>', views.detail, name="detail"),
    path("create_comment/<int:post_id>", views.create_comment, name="create_comment"),

    path("login", accounts_views.login, name="login"),
    path("logout", accounts_views.logout, name="logout"),
    path("register", accounts_views.register, name="register"),
    

    path('idHome', views.idHome, name="idHome"),
    path('idPostcreate', views.idPostcreate, name="idPostcreate"),
    path("idDetail/<int:post_id>", views.idDetail, name="idDetail"),
    path("new_idComment/<int:post_id>", views.new_idComment, name="new_idComment"),

    path("accounts/", include('allauth.urls')),
]


