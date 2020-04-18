# Generated by Django 3.0.4 on 2020-04-18 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('userID', models.CharField(max_length=10, unique=True, verbose_name='아이디')),
                ('username', models.CharField(blank=True, max_length=10, null=True, verbose_name='유저이름')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='연락처')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='이미지')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('question', models.CharField(blank=True, max_length=30, null=True)),
                ('answer', models.CharField(blank=True, max_length=200, null=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='보호소이름')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='보호소 위치')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='보호소 전화번호')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='위도')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='경도')),
            ],
        ),
        migrations.CreateModel(
            name='ShelterInformation',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='보호소이름')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='보호소 위치')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='보호소 전화번호')),
                ('area', models.CharField(blank=True, max_length=300, null=True)),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='위도')),
                ('lng', models.FloatField(blank=True, null=True, verbose_name='경도')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('menu', models.BooleanField(verbose_name='잃어버렸어요 or 발견했어요')),
                ('species', models.CharField(max_length=30, verbose_name='품종')),
                ('date', models.DateField(blank=True, null=True, verbose_name='실종 날짜')),
                ('location', models.CharField(max_length=100, verbose_name='실종 위치')),
                ('feature', models.CharField(max_length=200, verbose_name='특징')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='이미지')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='이미지 url')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('up_date', models.DateTimeField(auto_now=True, null=True)),
                ('shelter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Shelter')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('comment', models.CharField(max_length=150, verbose_name='댓글')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('up_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
