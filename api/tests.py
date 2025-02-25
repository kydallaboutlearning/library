# api/test.py


"""Importing requirements"""
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from Books.models import Book
from utils.test_variable import *



# setting up variable for the apitest


# Create your tests here.
class APItest(APITestCase):
     @classmethod
     def setUpTestData(cls):
          cls.book = Book.objects.create(
               title = t_title,
               subtitle = t_subtitle,
               author = t_author,
               isbn = t_isbn
          )

     
     def testApiListView(self):
          response = self.client.get(reverse('book_list'))
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(Book.objects.count(), 1)
          self.assertContains(response, t_title)

