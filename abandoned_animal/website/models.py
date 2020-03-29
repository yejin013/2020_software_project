import os
import uuid as uuid
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.files import File
from django.db import models
from .file import download

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, userID, password, phone=None, username=None, question=None, answer=None):
        if not userID:
            raise ValueError('ID Required')

        user = self.model(userID=userID, phone=phone, username=username, question=question, answer=answer)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userID, password):
        user = self.create_user(userID, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )
    userID = models.CharField(unique=True, max_length=10, verbose_name = '아이디') #아이디
    username = models.CharField(max_length=10, null=True, blank=True, verbose_name='유저이름')
    password = models.CharField(max_length=20, verbose_name = '비밀번호')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name = '연락처')
    image = models.ImageField(blank=True, null=True, upload_to="profile", verbose_name = '이미지')
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    ONE = '기억에 남는 추억의 장소는?'
    TWO = '자신의 인생 좌우명은?'
    THREE = '자신의 보물 제1호는?'
    FOUR = '가장 기억에 남는 선생님 성함은?'
    FIVE = '추억하고 싶은 날짜가 있다면?'
    SIX = '유년시절 가장 생각나는 친구 이름은?'
    SEVEN = '인상 깊게 읽은 책 이름은?'
    EIGHT = '읽은 책 중에서 좋아하는 구절이 있다면?'
    NINE = '자신이 두번째로 존경하는 인물은?'
    TEN = '초등학교 때 기억에 남는 짝궁 이름은?'
    ELEVEN = '다시 태어나면 되고 싶은 것은?'
    TWELEVE = '내가 좋아하는 캐릭터는?'
    THIRTEEN = '자신의 반려동물의 이름은?'
    CHOICES = (
        (ONE, '기억에 남는 추억의 장소는?'),
        (TWO, '자신의 인생 좌우명은?'),
        (THREE, '자신의 보물 제1호는?'),
        (FOUR, '가장 기억에 남는 선생님 성함은?'),
        (FIVE, '추억하고 싶은 날짜가 있다면?'),
        (SIX, '인상 깊게 읽은 책 이름은?'),
        (SEVEN, '인상 깊게 읽은 책 이름은?'),
        (EIGHT, '읽은 책 중에서 좋아하는 구절이 있다면?'),
        (NINE, '자신이 두번째로 존경하는 인물은?'),
        (TEN, '초등학교 때 기억에 남는 짝궁 이름은?'),
        (ELEVEN, '다시 태어나면 되고 싶은 것은?'),
        (TWELEVE, '내가 좋아하는 캐릭터는?'),
        (THIRTEEN, '자신의 반려동물의 이름은?')
    )
    question = models.CharField(max_length=30, choices=CHOICES, default=ONE, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    # up_date = models.DateTimeField('date updated')
    # del_date = models.DateTimeField('date deleted')
    is_activate = models.BooleanField(default=True)

    USERNAME_FIELD = 'userID'

    objects=UserManager()

    def __str__(self):
        return self.userID

    def is_staff(self):
        "Is the user a memeber of staff?"
        return self.is_superuser

class ShelterManager(BaseUserManager):
    def create_shelter(self, name, address, phone):
        shelter = self.model(name=name, address=address, phone=phone)
        shelter.save(using=self._db)
        return shelter

class Shelter(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='보호소이름')
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name='보호소 위치')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='보호소 전화번호')

    objects=ShelterManager()

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )
    menu = models.BooleanField(verbose_name = '잃어버렸어요 or 발견했어요')
    species = models.CharField(max_length=30, verbose_name = '품종')
    date = models.DateField(null = True, blank=True, verbose_name = '실종 날짜')
    location = models.CharField(max_length=100, verbose_name = '실종 위치')
    feature = models.CharField(max_length=200, verbose_name = '특징')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="images", verbose_name = '이미지')
    image_url = models.URLField(blank=True, null=True, verbose_name='이미지 url')
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    up_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __int__(self):
        return self.id

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path)) #Trash 파일을 안남기기 위해 객체와 함께 파일 삭제
        super(Post, self).delete(*args, **kargs) #원래의 delete 함수 실행

    def save(self, *args, **kwargs):
        # ImageField에 파일이 없고, url이 존재하는 경우에만 실행
        if self.image_url and not self.image:
            image = self.image_url.split("/")[-1]
            if image:
                temp_file = download(self.image_url)
                file_name = urlparse(self.image_url).path.split('/')[-1]
                self.image.save(file_name, File(temp_file))
                super().save()
            else:
                super().save()
        else:
            super().save()

class Comment(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )
    comment = models.CharField(max_length=150, verbose_name = '댓글')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    up_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.comment

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)