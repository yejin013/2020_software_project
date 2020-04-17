from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import User, Post, Comment, Shelter
=======
from django.http import HttpResponseRedirect
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth, messages
from django.shortcuts import render, redirect

from .models import User, Post, Comment, Shelter, ShelterInformation
from django.contrib import auth
<<<<<<< HEAD
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .form import SignupForm,ChangeForm
=======
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871
from .form import SignupForm, PostForm, CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


import math

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

            return redirect(reverse('website:homePost'))
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
<<<<<<< HEAD
            request.session['user'] = user.id
            return redirect('/website')
=======
            return redirect(reverse('website:homePost'))
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871
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

<<<<<<< HEAD
@login_required
def myinfo_update(request):
    if request.method == 'POST':
        user = request.user
        # question = request.POST.get('question', '')
        # answer = request.POST.get('answer', '')
        old_password = request.POST.get('oldPw')
        new_password = request.POST.get('userPw')
        passwordChk = request.POST.get('userPwChk')
        phone = request.POST.get('phone')
        if user.check_password(old_password,user.password):
            if user.phone == phone:
                if new_password == passwordChk:
                    user.set_password(new_password)
                    user.save()
                    auth.login(request,user)
                else:
                    return(request,'mypage_Info.html',{'notice':'전화번호가 일치하지 않습니다.'})
            else:
                return(request,'mypage_Info.html',{'error':'비밀번호를 일치하지 않습니다.'})
        else:
            return(request,'mypage_Info.html',{'notice':'비밀번호를 잘못 입력하셨습니다.'})
    else:
        return render(request,'mypage_Info.html')

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

# def viewMessage(request,message_id):
#     if not request.user.is_authenticated:
#         return redirect('signin')
#     messages = get_object_or_404(Message,pk=message_id)
#     messages.isRead = True
#     messages.save()

#     #쪽지 1개씩 보는 경우-> html 나오면 수정
#     return render(request,'msg_receivelist.html')
=======
@login_required()
def logout(request):
    auth.logout(request)
    return redirect(reverse('website:homePost'))
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871

def homePost(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 12)
    page_range = 5
    try:
        post = paginator.page(page)
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except PageNotAnInteger:
        post = paginator.page(1)
        current_block = math.ceil(int(1) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
        current_block = math.ceil(int(paginator.num_pages) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    return render(request, 'home.html', {'post' : post, 'p_range':p_range}) # 데이터 튜플로 들어감!

@csrf_exempt
def home2(request):
    if request.method == "POST":
        image = request.FILES['image']
        species = request.POST.get('species', '')
        inputState = request.POST.get('inputState', '')
        inputCity = request.POST.get('inputCity', '')
        location = inputState + ' ' + inputCity
        inputDate = request.POST.get('inputDate', '')
        return render(request, 'home_result.html', {'image' : image, 'species':species, 'location' : location, 'date':inputDate})

    else:
        return render(request, 'home2.html')

def findBoard(request):
    posts = Post.objects.filter(menu=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 12)
    page_range = 5
    try:
        post = paginator.page(page)
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except PageNotAnInteger:
        post = paginator.page(1)
        current_block = math.ceil(int(1) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
        current_block = math.ceil(int(paginator.num_pages) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    return render(request, 'findboard.html', {'post' : post, 'p_range':p_range})

def missBoard(request):
    posts = Post.objects.filter(menu=False)
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 12)
    page_range = 5
    try:
        post = paginator.page(page)
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except PageNotAnInteger:
        post = paginator.page(1)
        current_block = math.ceil(int(1) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
        current_block = math.ceil(int(paginator.num_pages) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    return render(request, 'missboard.html', {'post' : post, 'p_range':p_range})

def posterBoard(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 12)
    page_range = 5
    try:
        post = paginator.page(page)
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except PageNotAnInteger:
        post = paginator.page(1)
        current_block = math.ceil(int(1) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
        current_block = math.ceil(int(paginator.num_pages) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    return render(request, 'posterboard.html', {'post' : post, 'p_range':p_range})

def search(request):
    return render(request, '')

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
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.up_date = timezone.now()
                post.save()
                return redirect('post', id=post.uuid)
        else:
            form = PostForm(instance=post)
            if post.menu == True:
                return render(request, 'loseModify.html', {'form' : form})
            else :
                return render(request, 'findModify.html', {'form' : form})

def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
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
<<<<<<< HEAD
        return redirect('post', pk=comment.post.pk)
=======
        return redirect(reverse('website:postCheck', args=[str(post.id)]))

class ShelterDist:
    mylat = 0
    mylng = 0
    shelterlat = 0
    shelterlng = 0
    short = 0
    showlat = 0
    showlng = 0
    count = 0

    def __init__(self, lat, lng):
        self.mylat = float(lat)
        self.mylng = float(lng)

    def rad(self, x):
        return x * math.pi / 180

    def distHaversine(self, shelterlat, shelterlng):
        self.shelterlat = shelterlat
        self.shelterlng = shelterlng
        R = 3960
        dLat = self.rad(self.shelterlat - self.mylat)
        dLong = self.rad(self.shelterlng - self.mylng)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(self.rad(self.mylat)) * math.cos(self.rad(self.shelterlat)) * math.sin(dLong / 2) * math.sin(dLong / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        if self.count == 0:
            self.short = '{:0.1f}'.format(d)
        self.compareDistance('{:0.1f}'.format(d))
        self.count += 1

    def compareDistance(self, distance):
        if self.short >= distance:
            self.short = distance
            self.showlat = self.shelterlat
            self.showlng = self.shelterlng

def shelterInformation(request):
    lat = request.GET.get('lat', '0')
    lng = request.GET.get('lng', '0')

    list = ShelterInformation.objects.values()
    dist = ShelterDist(lat, lng)

    if (lat != '0') | (lng != '0'):
        for i in list:
            dist.distHaversine(i['lat'], i['lng'])
        lat_new = dist.showlat
        lng_new = dist.showlng

        information = ShelterInformation.objects.get(lat = lat_new, lng = lng_new)

        return render(request, 'shelter.html', {'information': information, 'lat': lat_new, 'lng': lng_new})
    return render(request, 'shelter.html')
>>>>>>> ab25f280aa52591a9761bb4cc11081b07b161871
