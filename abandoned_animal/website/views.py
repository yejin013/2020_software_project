from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import User, Post, Comment, Animal
from django.contrib import auth, messages
from django.views.decorators.http import require_http_methods
from .form import RegisterForm, PostForm

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

def create(request):
    post = Post()
    post.menu = request.GET['menu']
    post.species = request.GET['species']
    post.miss_date = request.GET['miss_date']
    post.miss_loc = request.GET['miss_loc']
    post.feature = request.GET['feature']
    post.request = request.GET['user']
    post.image = request.GET['image']
    post.pub_date = timezone.datetime.now()
    post.up_date = timezone.datetime.now()
    post.user = request.user.uuid
    post.save()
    return redirect('/post/' +str(post.id))

# 포스트한 내용 보여주기
def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post.html', {'post':post}) 

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

def animalPost(request):
    animalPost = Animal.objects.all()
    return render(request, 'html', { 'post' : animalPost }) # 데이터 튜플로 들어감!