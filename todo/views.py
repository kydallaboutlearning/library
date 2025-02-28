'todo/views'


"""Importing requirements"""
from django.shortcuts import render
from api.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Todo


"""Create your views here."""

# CReating a list view
class TodoList(APIView):
     def get(self,request,pk):
          max_objects = 20
          todos = Todo.objects.all()[:max_objects]
          data = TodoSerializer(todos,many = True)
          return Respomse(data)