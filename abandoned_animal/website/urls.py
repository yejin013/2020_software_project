from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
<<<<<<< HEAD
    path('register/', views.register, name='register'),
    path('db/', animalDB.db, name='db')
=======
    path('signup/', views.signup, name='signup')
>>>>>>> f/signup
]