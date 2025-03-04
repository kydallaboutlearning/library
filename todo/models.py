from django.db import models
from django.utils import timezone
from django.utils.timesince import timeuntil

# Create your models here.
class Todo(models.Model):
     task = models.CharField(max_length = 150)
     body = models.CharField(max_length = 5000)
     start_date = models.DateTimeField()
     end_date = models.DateTimeField()
     completed = models.BooleanField(default=False)



     @property
     def duration(self):
          return timeuntil(d=self.start_date,now=self.end_date,depth=4)
     
     # returning the title of the todo
     def __str__(self):
          return self.task
