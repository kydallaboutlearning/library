from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status 
from django.contrib.auth import get_user_model
from utils.test_variable import *
from django.urls import reverse

# Create your tests here.
class AccouuntApiTest(APITestCase):
     # setting up the tesr data
     def setup(self):
          self.user = user.objects.create_user(username = t_username,password = t_password)

     # testing userlist 
     def test_user_list(self):
          #authenticating user
          self.client.force_authenticate(user=self.user)

          # getting response
          response = self.client.get("/api/accounts/")
          
          # asserting the euality
          self.assertEqual(response.status_code, status.HTTP_200_OK)

