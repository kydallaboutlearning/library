# todo/test.py

from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Todo
from utils.test_variable import *
from django.utils import timezone


now = timezone.now()

# Create your tests here.
class todoModelTest(TestCase):
     @classmethod
     def setUpTestData(cls):
          cls.todo  = Todo.objects.create(
               task = t_title,
               body = t_body,
               start_date = now,
               end_date = now,
               completed = True
          )

     def test_model_content(self):
          self.assertEqual(self.todo.task,t_title)
          self.assertEqual(self.todo.body, t_body)
          self.assertEqual(self.todo.start_date,now)
          self.assertEqual(self.todo.end_date,now)
          self.assertTrue(self.todo.completed)
          # self.assertEqual(self.todo.duration(),0 )
     

     
     # creating test for theapi
     def test_todo_api_listview(self):
          response = self.client.get(reverse('todo-list'))
          self.assertEqual(response.status_code,status.HTTP_200_OK)
          self.assertEqual(Todo.objects.count(),1)
          # self.assertContains(response.content,self.todo)

     # creating a test fo
     def test_todo_api_detailview(self):
          # getting  the response
          response = self.client.get(reverse('todo-detail',kwargs={"pk":self.todo.id}),format ='json')
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(Todo.objects.count(),1)
          # self.assertContains(response,t_title)



          


          
