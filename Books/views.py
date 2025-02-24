from django.shortcuts import render
from  .models import Book

# Create your views here.

def HomeView(request):
     books = Book.objects.all()
     return render(request,'home/home.html',{'books':books})

