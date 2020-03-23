from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, animalDB

app_name = 'website'

urlpatterns = [
    path('db/', animalDB.db, name='db'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    path('login/findID/',views.findID,name='findID'),
    # path('login/findPW/',views.findPW,name='findPW'),
    path('', views.homePost, name='homePost'),
    path('create/', views.create, name='create'),
    path('detail/<int:post_id>', views.postCheck, name='post'),
    path('detail/edit/<int:post_id>', views.edit, name='edit'),
    path('detail/delete/<int:post_id>', views.delete, name='delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name="comment_delete"),
    path('comment/edit/<int:comment_id>/', views.comment_edit, name="comment_update"),
    path('mypage/',views.mypage,name='mypage'),
    path('mypage/myinfo/',views.myinfo_update,name='myinfo_update'),
    path('mypage/mypost/',views.listMypost,name='mypost'),
    path('mypage/mymessage/',views.listMessage,name='mymessage'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
