from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.post, name='post'),
    path('/', views.animalPost, name='animalPost'),
    path('db/', animalDB.db, name='db')
]