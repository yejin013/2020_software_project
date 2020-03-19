from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render, redirect,get_object_or_404
from .models import User,Message,Post
=======
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import User, Post, Comment, Shelter
from django.contrib import auth, messages
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import User, Post, Comment, Shelter
>>>>>>> c7c8b88f35a40c423356836e1a90cad92af39f96
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
<<<<<<< HEAD
from .form import SignupForm,ChangeForm
=======
from .form import SignupForm, PostForm, CommentForm
>>>>>>> c7c8b88f35a40c423356836e1a90cad92af39f96

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

<<<<<<< HEAD
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
=======
def homePost(request):
    post = Post.objects.all()
    return render(request, 'home.html', { 'post' : post }) # 데이터 튜플로 들어감!

@login_required()
def create(request):
    if request == "POST":
        post = Post()
        post.menu = request.POST['menu']
        post.species = request.POST['species']
        post.miss_date = request.POST['miss_date']
        post.miss_loc = request.POST['miss_loc']
        post.feature = request.POST['feature']
        post.request = request.POST['user']
        post.image = request.FILES['image']
        post.pub_date = timezone.datetime.now()
        post.up_date = timezone.datetime.now()
        post.user = request.user.id
        post.save()
        return render(request, 'postCheck.html', {'post': post})

    else:
        return render(request, 'postWrite.html')

# 포스트한 내용 보여주기
def postCheck(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    return render(request, 'postCheck.html', {'post': post, 'comments': comments})

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user.id
            comment.post = request.post.id
            comment.pub_date = timezone.datetime.now()
            comment.up_date = timezone.datetime.now()
            comment.save()
            return redirect('post', pk=post.id)
    else:
        comments = post.comments.all()

    # return render(request, 'post.html', {'post':post, 'comment_form':comment_form, 'comments':comments})
    return render(request, 'post.html', {'post':post, 'comments':comments})

# 포스트 수정, 구체적 form은 html에 맞춰서 수정 필요
def edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        messages.warning(request, "권한 없음")
        return redirect(post)
    else:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.up_date = timezone.now()
                post.save()
                return redirect('post', id=post.uuid)
        else:
            form = PostForm(instance=post)
            return render(request, 'html', form)

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        messages.warning(request, "권한 없음")
        return redirect(post)
    else:
        post.delete()
    return redirect('/')

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post', pk=comment.post.pk)

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.id)

    if request.user != comment.user:
        messages.warning(request, "권한 없음")
        return redirect(post)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect(post)
    else:
        form = CommentForm(instance=comment)
    return render(request, '.html', {'form': form})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = get_object_or_404(Post, pk=comment.post.id)

    if request.user != comment.user:
        messages.warning(request, "권한 없음")
        return redirect(post)
    else:
        comment.delete()
        return redirect('post', pk=comment.post.pk)
>>>>>>> c7c8b88f35a40c423356836e1a90cad92af39f96
