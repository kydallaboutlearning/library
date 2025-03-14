# api/serializer-

""" Importing requirements for the serializer"""
from rest_framework import serializers

# importing the modelsz from books
from Books.models import Book

# importing models  from todo
from todo.models import Todo 

# Importing models drom Blog
from blog.models import Post

# importing models for users
from django.contrib.auth import get_user_model


# Builiding the serializer
class BookSerializer(serializers.ModelSerializer):
    
     class Meta:
          model = Book
          fields = ('title','subtitle','author','isbn')


class TodoSerializer(serializers.ModelSerializer):
     class Meta:
          model = Todo
          fields = '__all__'

     
class BlogApiSerializer(serializers.ModelSerializer):
     class Meta:
          model = Post
          fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
     class Meta:
          model = get_user_model()
          fields = ('id','first_name','last_name','age','username')