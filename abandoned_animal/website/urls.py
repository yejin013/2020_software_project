from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('/<int:post_id>', views.post, name='post')
]