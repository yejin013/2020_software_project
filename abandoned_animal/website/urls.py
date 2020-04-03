from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
    path('db/', animalDB.db, name='db'),
    path('signup/', views.signup, name='signup'),
<<<<<<< HEAD
    path('login/',views.login,name='login'),
    path('', views.homePost, name='homePost'),
    path('search/', views.search, name='search'),
    path('findBoard/', views.findBoard, name='findBoard'),
    path('missBoard/', views.missBoard, name='missBoard'),
=======
    path('login/', views.login, name='login'),
    path('postFind/', views.postFind, name='postFind'),
    path('postLose/', views.postLose, name='postLose'),
>>>>>>> 98cfe092cd5c655c0414904b42c3ee99c7980fc8
    path('detail/<int:post_id>', views.postCheck, name='postCheck'),
    path('detail/edit/<int:post_id>', views.edit, name='edit'),
    path('detail/delete/<int:post_id>', views.delete, name='delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),
<<<<<<< HEAD
    path('comment/edit/<int:comment_id>/', views.comment_edit, name="comment_update"),
=======
    path('comment/edit/<int:comment_id>/', views.comment_edit, name="comment_edit"),
    path('', views.homePost, name='homePost'),
>>>>>>> 98cfe092cd5c655c0414904b42c3ee99c7980fc8
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
