# blog/tests.py



"""Importing Requirements"""
from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Post
from utils.test_variable import *


# Create your tests here.
class BlogApiTest(APITestCase):
     @classmethod
     def setUpTestData(cls):
          # setting up test user
          cls.t_user = user.objects.create(
               username = t_username,
               email = t_email,
               password = t_password,
               age = t_age
          )
          
          cls.post = Post.objects.create(
               title = t_title,
               author = cls.t_user,
               body = t_body
          )

     def testPostModel(self):
          self.assertEqual(self.post.title ,t_title)
          self.assertEqual(self.post.body, t_body)
          self.assertEqual(self.post.author.username, t_username)
          self.assertEqual(self.post.author.email, t_email)

          # self.assertEqual(self.post.created_at, t_time)
          # self.assertContains(self.post.slug,self.post.publish)
          # self.assertEqual(self.post.status,'Post.Status.DRAFT')


