# blog/tests.py



"""Importing Requirements"""
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Post
from utils.test_variable import *


# Create your tests here.
class BlogApiTest(APITestCase):
     @classmethod
     def setUpTestData(cls):
          cls.post = Post.objects.create(
               title = t_title,
               author = t_user,
               body = t_body
          )

     def testPostModel(self):
          self.assertEqual(self.post.title ,t_title)
          self.assertEqual(self.post.body, t_body)
          self.assertEqual(self.post.created, t_time)
          self.assertContains(self.post.slug,self.post.publish)
          self.assertEqual(self.post.status,'DRAFT')


