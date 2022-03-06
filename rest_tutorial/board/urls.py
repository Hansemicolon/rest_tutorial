from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from .views import CustomBoardList

urlpatterns = [
    path("", views.index, name='index'),
    path("viewjson/", views.viewjson, name='viewjson'),
    path('boardlist/', views.boardList, name='boardlist'),
    path('boardlist/<str:mbti>', CustomBoardList.as_view(), name='boardview'),
    path('boardinsert/', views.boardInsert, name='boardinsert'),
    path('boardupdate/<str:user_name>/', views.boardUpdate, name='boardupdate')
]
