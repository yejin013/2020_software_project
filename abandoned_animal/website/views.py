from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from django.contrib import auth, messages
from django.shortcuts import render, redirect

from .models import User, Post, Comment, Shelter, ShelterInformation, Message
from django.contrib import auth
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .form import SignupForm, PostForm, CommentForm, MessageForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist


import math
import string
import random

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
            return redirect(reverse('website:homePost'))
        else:
            return render(request,'login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'login.html')

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
    Usermodel = get_user_model()
    if request.method == "POST":
        userID = request.POST.get('name', '')
        question = request.POST.get('findQuestion', '')
        answer = request.POST.get('findAnswer', '')
        
        user = Usermodel.objects.filter(userID=userID,question=question,answer=answer)
        if user is not None:
            _LENGTH = 10
            string_pool = string.digits
            new_password = ""
            for i in range(_LENGTH):
                new_password += random.choice(string_pool)
            user = authenticate(username=user.userID,password=user.password)
            user.set_password(new_password)
            user.save()
            user = None 
            return render(request,'answerPW.html',{'newPW':new_password})
        else:
            return render(request,'findPW.html',{'error':'회원 정보가 존재하지 않습니다.'})
    else:
        return render(request,'findPW.html')

@login_required()
def logout(request):
    auth.logout(request)
    return redirect(reverse('website:homePost'))

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

@login_required
def mypage(request):
    user = request.user
    if user:
        return render(request,'mypage_main.html',{'user': user})
    else:
        return render(request,'login.html')

@login_required
def myinfo_update(request):
    if request.method == "POST":
        user = request.user
        image = request.FILES
        question = request.POST.get('findQuestion', '')
        answer = request.POST.get('findAnswer', '')
        old_password = request.POST.get('oldPw','')
        new_password = request.POST.get('userPw','')
        passwordChk = request.POST.get('userPwChk','')
        phone = request.POST.get('phone','')
        if 'image_submit' in request.POST:
            if image is not None :
                user.image = request.FILES['image']
                user.save()
                return render(request,'mypage_Info.html',{'notice':'수정이 완료되었습니다.'})
            else:
                return render(request,'mypage_Info.html',{'error':'잘못 입력하셨습니다.'})
        else: 
            if check_password(old_password,user.password)is False or phone != user.phone or question != user.question or answer != user.answer:
                return render(request,'mypage_Info.html',{'error':'입력한 기존 정보가 잘못되었습니다.'})
            else:
                if new_password != passwordChk:
                    return(request,'mypage_Info.html',{'error':'잘못 입력하셨습니다.'})
                else:
                    user.set_password(new_password)
                    user.save()
                    auth.login(request,user)
                    return render(request,'mypage_Info.html',{'notice':'수정이 완료되었습니다.'})
    else:
        return render(request,'mypage_Info.html') 

@login_required
def user_delete(request,user_id):
    user = request.user
    if user is not None:
        user.delete()
        logout(request)
        messages.success(request,"회원탈퇴가 완료되었습니다.")
        return redirect(reverse('website:homePost'), args=[str(user.id)])
    else:
        messages.warning(request, "권한 없음")
        return redirect(reverse('website:homePost', args=[str(user.id)]))

@login_required
def mypost(request):
    posts = Post.objects.filter(user=request.user)
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
    return render(request, 'mypost.html', {'post' : post, 'p_range':p_range})

@login_required
def myMessage(request):
    if request.method == "POST":
        msg_form = MessageForm(request.POST)
        recipient1 = request.POST['recipient']
        try:
            recipient1 = User.objects.get(userID=recipient1)
        except ObjectDoesNotExist:
            return render(request,'msg_write.html',{'error':'User NONE'})
            
        if recipient1 is not None:
            if msg_form.is_valid():
                message = msg_form.save(commit=False)
                message.sender = request.user
                message.recipient = User.objects.get(userID=recipient1)
                message.content = request.POST['content']
                message.save()            
                return render(request,'msg_write.html')
            else:
                return render(request,'msg_write.html',{'error':'validation wrong'})
        else:
            return render(request,'msg_write.html',{'error':'User NONE'})
        
    else:
        form = MessageForm()
        return render(request,'msg_write.html',{'form':form})

@login_required
def receiveListMsg(request):
    r_msgs = Message.objects.filter(recipient = request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(r_msgs, 12)
    page_range = 5
    try:
        rList = paginator.page(page)
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except PageNotAnInteger:
        rList = paginator.page(1)
        current_block = math.ceil(int(1) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except EmptyPage:
        rList = paginator.page(paginator.num_pages)
        current_block = math.ceil(int(paginator.num_pages) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]

    return render(request,'msg_receivelist.html',{'rlist':rList, 'p_range':p_range})

@login_required
def sendListMsg(request):
    s_msgs = Message.objects.filter(sender = request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(s_msgs, 12)
    page_range = 5
    try:
        sList = paginator.page(page)
        current_block = math.ceil(int(page) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except PageNotAnInteger:
        sList = paginator.page(1)
        current_block = math.ceil(int(1) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    except EmptyPage:
        sList = paginator.page(paginator.num_pages)
        current_block = math.ceil(int(paginator.num_pages) / page_range)
        start_block = (current_block - 1) * page_range
        end_block = start_block + page_range
        p_range = paginator.page_range[start_block:end_block]
    return render(request,'msg_sendlist.html',{'slist':sList, 'p_range':p_range})