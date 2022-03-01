from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("viewjson/", views.viewjson, name='viewjson'),
    path('boardlist/', views.boardList, name='boardlist'),
    path('boardlist/<str:mbti>', views.boardView, name='boardview')
]
