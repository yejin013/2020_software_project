from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import User, Post, Comment, Shelter
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import User, Post, Comment, Shelter
from django.contrib import auth, messages
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import User, Post, Comment, Shelter
from django.contrib import auth
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .form import SignupForm,ChangeForm
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
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = user.id
            return redirect('/website')
        else:
            return render(request,'login.html',{'error':'아이디 혹은 비밀번호를 잘못 입력하였습니다.'})
    else:
        return render(request,'login.html')

# 로그인 유지 - 세션에 user정보 존재시
def home_login(request):
    userID = request.session.get('user')
    if userID:
        user = User.objects.get(id=userID)
        return render(request,'home.html',{'user': user})
    else:
        return render(request,'home.html')

def findID(request):
    Usermodel = get_user_model()
    if request.method == "POST":
        username = request.POST['username']
        phone = request.POST['phone']
        try:
            user1 = Usermodel.objects.get(username=username)
            user2 = Usermodel.objects.get(phone=phone)
        except ObjectDoesNotExist:  
            return render(request,'findID.html',{'error':'회원 정보가 존재하지 않습니다.'})
       
        if user1 != user2:
            return render(request,'findID.html',{'error':'회원 정보가 존재하지 않습니다.'})
        else:
            return render(request,'answerID.html',{'user':user1})       
    else:
        return render(request,'findID.html')

def findPW(request):
    if request.method == "POST":
        userID = request.POST['userID']
        
        user = User.objects.all().filter(username=userID)
        if userID is not None:
            return render(request,'answerPW.html',{'user':user})
        else:
            return render(request,'findPW.html',{'error':'회원 정보가 존재하지 않습니다.'})
    else:
        return render(request,'findPW.html')


@login_required
def mypage(request):
    user_id = request.session.get('user')
    if id:
        user = User.objects.get(id=user_id)
        return render(request,'mypage_main.html',{'user': user})
    else:
        return render(request,'login.html')

@login_required
def myinfo_update(request):
    if request.method == 'POST':
        user = request.user
        new_password = request.POST.get('password')
        passwordChk = request.POST.get('passwordChk')
        current_password = request.POST.get('origin_password')
        phone = request.POST.get('phone')
        findAnswer = request.POST.get('findAnswer')
        if user.check_password(current_password,user.password):
            if new_password == passwordChk:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
            #html 이름 변경시 수정 필요
            return redirect(request,'update.html')
        else:
            return(request,'update.html',{'error':'비밀번호 일치x'})
    else:
        #html 이름 변경시 수정 필요
        return render(request,'update.html',{'user_change_form':user_change_form})

@login_required
def listMypost(request):
    user_id = request.session.get('user')
    mypost = Post.objects.filter(user=user_id).ordered_by('pub_date')
    
    #html 나오면 수정필요 + 이 list도 두가지로 나눌 것인가?
    return render(request,'내포스트.html',{'post':mypost})

# def sendMessage(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)

#         if form.is_valide():
#             message = form.save(commit)

# @login_required
# def listMessage(request):
    # receivedList = Message.objects.filter(receiver = request.user)
    # sentList = Message.objects.filter(sender = request.user)

    #쪽지함 List html 나오면 수정
    # return render(request,'쪽지함.html',{'rlist':receivedList,'slist':sentList})

def viewMessage(request,message_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    messages = get_object_or_404(Message,pk=message_id)
    messages.isRead = True
    messages.save()

    #쪽지 1개씩 보는 경우-> html 나오면 수정
    return render(request,'msg_receivelist.html')

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
