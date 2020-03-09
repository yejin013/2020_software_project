# Generated by Django 3.0.3 on 2020-03-09 06:15

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
                ('username', models.CharField(max_length=10, unique=True, verbose_name='아이디')),
                ('password', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('phone', models.CharField(max_length=11, verbose_name='연락처')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('menu', models.BooleanField(verbose_name='잃어버렸어요 or 발견했어요')),
                ('species', models.CharField(max_length=30, verbose_name='품종')),
                ('miss_date', models.DateTimeField(blank=True, null=True, verbose_name='실종 날짜')),
                ('miss_loc', models.CharField(max_length=100, verbose_name='실종 위치')),
                ('feature', models.CharField(max_length=200, verbose_name='특징')),
                ('shelter', models.CharField(max_length=30, verbose_name='보호소')),
                ('shelter_phone', models.CharField(max_length=20, verbose_name='보호소 전화번호')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='이미지')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('up_date', models.DateTimeField(auto_now_add=True, null=True)),
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
