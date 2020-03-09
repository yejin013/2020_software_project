from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .form import RegisterForm

# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.setpassword(register_form.cleaned_data['password'])
            user.save()

            username = user.username

            return render(request, 'register.html', {'username' : username})
    else:
        register_form = RegisterForm()
        return render(request, 'register.html', {'form':register_form})
'''
@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user = registerform.save(commit=False)  # ajax로 아이디 중복 체크 만들기
            user.email = registerform.cleaned_data['email']
            user.password = registerform.cleaned_data['password']
            user.phone = registerform.cleaned_data['phone']
            user.save()
            username = user.username
            """
            username = signupform.save(commit=False) #ajax로 아이디 중복 체크 만들기
            email = signupform.cleaned_data['email']
            password = signupform.cleaned_data['password']
            phone = signupform.cleaned_data['phone']
            new_user = User.objects.create_user(username, email, phone, password=password)
            new_user.save()
            """
            return render(request, 'register.html', {'username' : username})
        else:
            return HttpResponse("잘못된 접근")
            # return render(request, '.html', {'signupform':signupform,})
    elif request.method == 'GET':
        return render(request, 'register.html')
'''
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

    