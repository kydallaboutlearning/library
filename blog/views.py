from django.shortcuts import render
from rest_framework import generics
from api.serializers import BlogApiSerializer
from .models import Post

# Create your views here.
class BlogListView(generics.ListCreateAPIView):
     queryset = Post.objects.all()
     serializer_class = BlogApiSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Post.objects.all()
     serializer_class = BlogApiSerializer
