from django.shortcuts import render
from rest_framework import (
                         generics,
                         permissions
                    )
from api.serializers import BlogApiSerializer
from .models import Post
from api.permissions import *

# Create your views here.
class BlogListView(generics.ListCreateAPIView):
     queryset = Post.objects.all()
     serializer_class = BlogApiSerializer
     permission_classes = (IsAuthororReadOnly,)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
     permission_class = permissions.IsAdminUser
     queryset = Post.objects.all()
     permission_classes = (IsAuthororReadOnly,)
     serializer_class = BlogApiSerializer
