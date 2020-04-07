from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, animalDB, web_shelter

app_name = 'website'

urlpatterns = [
    path('db/', animalDB.db, name='db'),
    path('shelterDb/', web_shelter.shelterDB, name='shelterDB'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('', views.homePost, name='homePost'),
    path('search/', views.search, name='search'),
    path('findBoard/', views.findBoard, name='findBoard'),
    path('missBoard/', views.missBoard, name='missBoard'),
    path('posterBoard/', views.posterBoard, name='posterBoard'),
    path('postFind/', views.postFind, name='postFind'),
    path('postLose/', views.postLose, name='postLose'),
    path('detail/<int:post_id>', views.postCheck, name='postCheck'),
    path('detail/edit/<int:post_id>', views.edit, name='edit'),
    path('detail/delete/<int:post_id>', views.delete, name='delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('comment/edit/<int:comment_id>/', views.comment_edit, name="comment_edit"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
