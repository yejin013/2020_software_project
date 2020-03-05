from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('db/', animalDB.db, name='db')
]