import os
import uuid as uuid

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError('ID Required')

        user = self.model(username = username, phone = kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
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
    username = models.CharField(unique=True, max_length=10, verbose_name = '아이디') #아이디
    password = models.CharField(max_length=20, verbose_name = '비밀번호')
    phone = models.CharField(max_length=11, verbose_name = '연락처')
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # up_date = models.DateTimeField('date updated')
    # del_date = models.DateTimeField('date deleted')
    is_activate = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    objects=UserManager()

    def __str__(self):
        return self.username

    def is_staff(self):
        "Is the user a memeber of staff?"
        return self.is_superuser

class Post(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )
    menu = models.BooleanField(verbose_name = '잃어버렸어요 or 발견했어요')
    species = models.CharField(max_length=30, verbose_name = '품종')
    miss_date = models.DateTimeField(null = True, blank=True, verbose_name = '실종 날짜')
    miss_loc = models.CharField(max_length=100, verbose_name = '실종 위치')
    feature = models.CharField(max_length=200, verbose_name = '특징')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    shelter = models.CharField(max_length=30, verbose_name='보호소')
    shelter_phone = models.CharField(max_length=20, verbose_name = '보호소 전화번호')
    image = models.ImageField(blank=True, null=True, upload_to="", verbose_name = '이미지')
    # url = models.URLField(blank=True, null=True, max_length=200, verbose_name = '보호소 이미지')
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    up_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __int__(self):
        return self.id

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path)) #Trash 파일을 안남기기 위해 객체와 함께 파일 삭제
        super(Post, self).delete(*args, **kargs) #원래의 delete 함수 실행

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

'''
class Animal(models.Model):
    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
        verbose_name='pk'
    )
    age = models.CharField(max_length=10)
    careaddr = models.CharField(max_length=300)
    carenm = models.CharField(max_length=100)
    caretel = models.CharField(max_length=15)
    colorcd = models.CharField(max_length=20)
    kindcd = models.CharField(max_length=50)
    specialmark = models.CharField(max_length=300)
'''