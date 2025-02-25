# api/serializer-

""" Importing requirements for the serializer"""
from rest_framework import serializers

from Books.models import Book

# Builiding the serializer
class BookSerializer(serializers.ModelSerializer):
    
     class Meta:
          model = Book
          fields = ('title','subtitle','author','isbn')