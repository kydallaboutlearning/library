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
from rest_framework.permissions import IsAdminUser

"""# Create your views here."""
from rest_framework.viewsets import ViewSet, ModelViewSet

# usserist api viewSET
class UserViewSet(ModelViewSet):
     permission_classes = (IsAdmin,)
     queryset = get_user_model().objects.all()
     serializer_class = UserSerializer

