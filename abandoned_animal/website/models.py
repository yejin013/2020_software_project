import uuid as uuid
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
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='PK'
    )
    username = models.CharField(unique=True, max_length=10, verbose_name = '아이디') #아이디
    password = models.CharField(max_length=20, verbose_name = '비밀번호')
    phone = models.CharField(max_length=11, verbose_name = '연락처')
    pub_date = models.DateTimeField(auto_now_add=True)
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
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='PK'
    )
    species = models.CharField(max_length=30, verbose_name = '품종')
    miss_date = models.DateTimeField(verbose_name = '실종 날짜')
    miss_loc = models.CharField(max_length=100, verbose_name = '실종 위치')
    feature = models.CharField(max_length=200, verbose_name = '특징')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, verbose_name = '이미지')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

class Comment(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='PK'
    )
    comment = models.CharField(max_length=150, verbose_name = '댓글')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment