from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
     task = models.CharField(max_length = 150)
     body = models.CharField(max_length = 5000)
     start_date = models.DateTimeField(default=timezone.now())
     end_date = models.DateTimeField(default=timezone.now())
     completed = models.BooleanField(default=False)


     # returning the title of the todo
     @property
     def duration(self):
          duration = self.start_date - self.end_date
          return duration

     def __str__(self):
          return self.task
