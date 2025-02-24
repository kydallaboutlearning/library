from django.urls import path
from .views import HomeView

# setting urlPATTERNS
urlpatterns = [
     path('',HomeView,name='home')
]