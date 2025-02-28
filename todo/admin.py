# todo/views.py

"""Importing requirements"""
from django.contrib import admin
from .models import Todo

# Register your models here.
admin.site.register(Todo)


class registerAdmin(admin.ModelAdmin):
     class Meta:
          model = Todo
     list_display = ['start_date','end_date','completed']