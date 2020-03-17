from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
    path('db/', animalDB.db, name='db'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('', views.homePost, name='home')
]