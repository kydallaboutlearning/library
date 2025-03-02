from django.db import models
from django.conf import settings 
from django.utils import timezone

user = settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
     # CREATED A CHOICE FOR STATUS
     class Status(models.TextChoices):
          DRAFT ='Df', 'Draft'
          PUBBLISHED  = 'Pub', 'Published'


     author = models.ForeignKey(user,on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     slug = models.SlugField(max_length=250,unique_for_date='publish')
     body = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     publish = models.DateTimeField(default = timezone.now)
     
     status = models.CharField(
          max_length = 3,
          choices = Status.choices,
          default = Status.DRAFT
     )

     def __str__(self):
          return self.title

