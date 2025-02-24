from django.test import TestCase
from django.urls import reverse
from .models import Book

# setting up variables
t_title = "testtitle",
t_subtitle = "testSubtitle"
t_author = "testauthor"
t_isbn = "testisbn"

# Create your tests here.
class BookTest(TestCase):
     @classmethod
     def setUpTestData(cls):
          Book.object.create(
               title = t_title,
               subtitle = t_subtitle,
               author = t_author,
               isbn = t_isbn
          )