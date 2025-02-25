# api/views.py

"""Importing requirements for the views"""
from django.urls import path
from .views import BookApiView



# setting urlpaterns
urlpatterns = [
     path('', BookApiView.as_view(), name='book_list')
]