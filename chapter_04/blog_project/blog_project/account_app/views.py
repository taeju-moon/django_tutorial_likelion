from django.shortcuts import render, redirect
#authentication
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == "GET":
        #login.html을 띄워줌
        return render(request, "login.html")
    else:
        #로그인을 처리해줌
        userName = request.POST["username"]
        passWord = request.POST["password"]
        user = auth.authenticate(request,username=userName, password=passWord) #없으면 None을 반환
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")