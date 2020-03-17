from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User, Post, Comment, Shelter
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .form import SignupForm

# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('password', '')
        passwordChk = request.POST.get('passwordChk', '')
        phone = request.POST.get('phone', '')

        if password != passwordChk:
            return render(request, 'failure.html')

        else:
            User.objects.create_user(username=username, password = password, phone = phone)
        return render(request, 'home.html')
    else:
        return render(request, 'signup.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("로그인 성공")
        else:
            return render(request,'login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

def homePost(request):
    post = Post.objects.all()
    return render(request, 'home.html', { 'post' : post }) # 데이터 튜플로 들어감!