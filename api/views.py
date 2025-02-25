# api/views.py


"""Importing Requirements for the views"""
from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from Books.models import Book


# Create your views here.
class BookApiView(generics.ListAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer


