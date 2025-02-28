'todo/views'


"""Importing requirements"""
from django.shortcuts import render
from api.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Todo


"""Create your views here."""

# CReating a list view
class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer