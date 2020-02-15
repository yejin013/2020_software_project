from django.db import models

# Create your models here.

class Users(models.Model):
    nick = models.CharField(max_length=10) #아이디
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    pub_date = models.DateTimeField('date published')
    # up_date = models.DateTimeField('date updated')
    del_date = models.DateTimeField('date deleted')

    def __str__(self):
        return self.nick
