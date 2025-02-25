from django.test import TestCase
from django.urls import reverse
from .models import Book
from utils.test_variable import *



# Create your tests here.
class BookTest(TestCase):
     @classmethod
     def setUpTestData(cls):
          cls.book = Book.objects.create(
               title = t_title,
               subtitle = t_subtitle,
               author = t_author,
               isbn = t_isbn
          )

     
     def test_book_content(self):
          self.assertEqual(self.book.title,t_title)
          self.assertEqual(self.book.subtitle, t_subtitle)
          self.assertEqual(self.book.isbn, t_isbn)
          self.assertEqual(self.book.author, t_author)

     def test_book_url(self):
          response = self.client.get(reverse("home"))
          self.assertEqual(response.status_code, 200)
          self.assertContains(response, "All Books")
          self.assertTemplateUsed(response,'home/home.html')


