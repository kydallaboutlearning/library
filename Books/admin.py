from django.contrib import admin
# importing the models
from .models import Book


# Register your models here.
admin.site.register(Book)