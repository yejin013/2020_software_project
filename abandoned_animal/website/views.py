from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.http import require_http_methods
from .form import SignupForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save(commit=False)  # ajax로 아이디 중복 체크 만들기
            user.email = signupform.cleaned_data['email']
            user.password = signupform.cleaned_data['password']
            user.phone = signupform.cleaned_data['phone']
            user.save()
            """
            username = signupform.save(commit=False) #ajax로 아이디 중복 체크 만들기
            email = signupform.cleaned_data['email']
            password = signupform.cleaned_data['password']
            phone = signupform.cleaned_data['phone']
            new_user = User.objects.create_user(username, email, phone, password=password)
            new_user.save()
            """
            return HttpResponse("회원가입 성공")
            #return redirect('/')
        else:
            return HttpResponse("잘못된 접근")
            # return render(request, '.html', {'signupform':signupform,})