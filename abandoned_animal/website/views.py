from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import User,Message,Post
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .form import SignupForm,ChangeForm

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

@login_required
def mypage(request,username):
    if request.user.authenticated():
        return HttpResponse('mypage.html')
    else:
        return HttpResponse("로그인 필요") 
        #로그인 안하고 mypage 연결시 어떻게 할건지 결정필요

@login_required
def update(request):
    if request.method == 'POST':
        user_change_form = ChangeForm(request.POST,instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            #html 이름 변경시 수정 필요
            return redirect(request,'update.html')
    else:
        user_change_form = ChangeForm(instance=request.user)
        #html 이름 변경시 수정 필요
        return render(request,'update.html',{'user_change_form':user_change_form})

def listMypost(request):
    mypostList = Post.objects.filter(user=request.user)

    #html 나오면 수정필요 + 이 list도 두가지로 나눌 것인가?
    return render(request,'listMypost.html')

# def sendMessage(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)

#         if form.is_valide():
#             message = form.save(commit)

def listMessage(request):
    receivedList = Message.objects.filter(receiver = request.user)
    sentList = Message.objects.filter(sender = request.user)

    #쪽지함 List html 나오면 수정
    return render(request,'쪽지함.html',{'rlist':receivedList,'slist':sentList})

def viewMessage(request,message_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    messages = get_object_or_404(Message,pk=message_id)
    messages.isRead = True
    messages.save()

    #쪽지 1개씩 보는 경우-> html 나오면 수정
    return render(request,'쪽지보기.html',{'message':messages})