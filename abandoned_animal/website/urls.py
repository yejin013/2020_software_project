from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
    path('db/', animalDB.db, name='db'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.post, name='post'),
    path('detail/edit/<int:post_id>', views.edit, name='edit'),
    path('detail/delete/<int:post_id>', views.delete, name='delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('comment/edit/<int:comment_id>/', views.comment_edit, name="comment_update"),
    path('', views.homePost, name='homePost'),
]