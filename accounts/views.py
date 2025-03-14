# accounts/api.py

"""Importing requirements for the views"""

from django.shortcuts import render

# getting the serializers
from api.serializers import UserSerializer

# importing from the rst_framewor
from rest_framework  import generics

# importing the user model
from django.contrib.auth import get_user_model

# importing permission
from api.permissions import *

"""# Create your views here."""

# usserist api view
class UserListAPi(generics.ListCreateAPIView):
     queryset = get_user_model().objects.all()
     serializer_class = UserSerializer

#user details models 
class UserDetailAPi(generics.RetrieveDestroyAPIView):
     permission_classes = (IsAdmin,)
     queryset = get_user_model().objects.all()
     serializer_class = UserSerializer
