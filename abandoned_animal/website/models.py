import uuid as uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('ID Required')

        user = self.model(username = username)
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
    username = models.CharField(unique=True, max_length=10) #아이디
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
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
