from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import User, Post, Comment, Shelter
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .form import SignupForm, PostForm, CommentForm


# Create your views here.

@csrf_exempt
def signup(request):
    if request.method == "POST":
        userID = request.POST.get('userID', '')
        username = request.POST['username']
        password = request.POST.get('password', '')
        passwordChk = request.POST.get('passwordChk', '')
        phone = request.POST.get('phone', '')
        question = request.POST.get('question', '')
        answer = request.POST.get('answer', '')
        if password != passwordChk:
            return render(request, 'failure.html')

        else:
            user = User.objects.create_user(userID=userID, username=username, password = password, phone = phone, question = question, answer=answer)
            print(user.question)

            return render(request, 'home.html')
    else:
        return render(request, 'signup.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request, 'home.html')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

@login_required()
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

@login_required()
def postFind(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.menu = True
            post.pub_date = timezone.datetime.now()
            post.up_date = timezone.datetime.now()
            post.user = request.user
            post.save()
            return redirect(reverse('website:postCheck', args=[str(post.id)]))

    else:
        form = PostForm()
        return render(request, 'postFind.html', {'form' : form})

@login_required
def postLose(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.menu = True
        post.pub_date = timezone.datetime.now()
        post.up_date = timezone.datetime.now()
        post.user = request.user
        post.save()
        return redirect(reverse('website:postCheck', args=[str(post.id)]))

    else:
        form= PostForm()
        return render(request, 'postLose.html', {'form':form})

# 포스트한 내용 보여주기
def postCheck(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.comment = request.POST['comment']
            comment.user = request.user
            comment.post = post
            comment.pub_date = timezone.datetime.now()
            comment.up_date = timezone.datetime.now()
            comment.save()
            return render(request, 'postCheck.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
    else:
        comment_form = CommentForm()

    return render(request, 'postCheck.html', {'post': post, 'comments': comments, 'comment_form' : comment_form})

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
        return redirect(reverse('website:postCheck', args=[str(post.id)]))
    else:
        post.delete()
        return redirect(reverse('website:homePost'))

@login_required
def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Post, pk=comment.post.id)
    comments = post.comments.all()

    if comment.user.userID != request.user.userID:
        return redirect(reverse('website:postCheck', args=[post.id]))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment = request.POST['comment']
            comment.up_date = timezone.datetime.now()
            comment.save()
            return redirect(reverse('website:postCheck', args=[str(post.id)]))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_edit.html', {'form': form, 'comment':comment, 'comments':comments, 'post':post})

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post = get_object_or_404(Post, pk=comment.post.id)

    if request.user != comment.user:
        messages.warning(request, "권한 없음")
        return redirect(reverse('website:postCheck', args=[str(post.id)]))
    else:
        comment.delete()
        return redirect(reverse('website:postCheck', args=[str(post.id)]))

def homePost(request):
    post = Post.objects.all()
    return render(request, 'home.html', { 'post' : post }) # 데이터 튜플로 들어감!