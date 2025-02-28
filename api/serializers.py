# api/serializer-

""" Importing requirements for the serializer"""
from rest_framework import serializers

# importing the modelsz from books
from Books.models import Book

# importing models  from todo
from todo.models import Todo 


# Builiding the serializer
class BookSerializer(serializers.ModelSerializer):
    
     class Meta:
          model = Book
          fields = ('title','subtitle','author','isbn')


class TodoSerializer(serializers.ModelSerializer):
     class Meta:
          model = Todo
          fields = '__all__'