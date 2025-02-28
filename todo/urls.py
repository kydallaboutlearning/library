
"""Importing requirements for the models"""
from django.urls import path
from .views import TodoList, TodoDetail



# creating the urls
urlpatterns = [
     path('', TodoList.as_view() ,  name = 'todo-list'),
     path('<int:pk>/', TodoDetail.as_view(), name = 'todo-detail')
] 