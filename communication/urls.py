from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('', views.chatroom_list, name='chatroom_list'),
    path('create/', views.chatroom_create, name='chatroom_create'),
    path('<int:chatroom_id>/', views.chatroom_detail, name='chatroom_detail'),
]
