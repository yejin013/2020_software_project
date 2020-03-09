from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
]