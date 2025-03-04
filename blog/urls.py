from django.urls import path
from .views import *


# setting the url pattern
urlpatterns = [
     path('',BlogListView.as_view(), name = 'blog-list'),
     path('<int:pk>/',BlogDetailView.as_view(),name = 'blog-details')
]