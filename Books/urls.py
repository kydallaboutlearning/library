# Books/urls.py


""" Imporing requirements for the urls"""
from django.urls import path
from .views import HomeView

# setting urlPATTERNS
urlpatterns = [
     path('',HomeView,name='home')
]