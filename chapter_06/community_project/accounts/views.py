from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, "bad.html")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("home")

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        if request.POST["password"] != request.POST["repeatPassword"]:
            return render(request, "register.html")
        else:
            #회원가입
            new_user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            #로그인
            auth.login(request, new_user)
            return redirect("home")

