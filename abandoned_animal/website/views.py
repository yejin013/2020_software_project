from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .form import SignupForm

# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        phone = request.POST.get('phone', '')

        if password1 != password2:
            return render(request, 'failure.html')

        else:
            User.objects.create_user(username=username, password = password1, phone = phone)
        return render(request, 'home.html')
    else:
        return render(request, 'sign.html')

'''
@csrf_exempt
def register(request):
    if request.method == "POST":
        registerform = RegisterForm(request.POST)

        if registerform.is_valid():
            user = registerform.save(commit=False)
            user.setpassword(registerform.cleaned_data['password'])
            user.save()

            username = user.username
            return render(request, 'home.html', {'signupform' : registerform})
        return render(request, 'failure.html', {'signupform': registerform})
    else:
        register_form = RegisterForm()
        return render(request, 'sign.html', {'form' : register_form})
'''