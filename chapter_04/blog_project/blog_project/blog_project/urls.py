"""blog_project URL Configuration

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
from django.urls import path
from blog_app import views
from django.conf import settings
from django.conf.urls.static import static
from account_app import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),

    #html form을 이용해 blog 객체 만들기
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),

    #django form을 이용해 blog 객체 만들기
    path('formcreate/',views.formcreate, name="formcreate"),

    #django modelform을 이용해 blog 객체 만들기
    path('modelcreate/', views.modelcreate, name="modelcreate"),

    #127.0.0.1:8000/detail/PK
    #기본키(int 자료형)를 blog_id라는 인자로 detail에게 넘겨주겠다
    path('detail/<int:blog_id>', views.detail, name="detail"),

    #댓글 저장
    path('createcomment/<int:blog_id>', views.createcomment, name="createcomment"),

    path('login', account_views.login, name="login"),

    path("logout", account_views.logout, name="logout"),
]

#media 파일 접근할 수 있는 url 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

