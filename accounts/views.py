# accounts/api.py

"""Importing requirements for the views"""

from django.shortcuts import render

# getting the serializers
from api.serializers import UserSerializer

# importing from the rst_framewor
from rest_framework  import generics

# importing the user model
from django.contrib.auth import get_user_model

"""# Create your views here."""

# usserist api view
class UserListAPi(generics.ListAPIView):
     queryset = get_user_model
     serializer_class = UserSerializer

#user details models 
class UserDetailAPi(generics.ListAPIView):
     queryset = get_user_model
     serializer_class = UserSerializer
