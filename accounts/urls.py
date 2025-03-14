from django.urls import path
from .views import UserListAPi, UserDetailAPi


urlpatterns = [
     path('',UserListAPi.as_view(),name ='users-list'),
     path('<int:pk>/',UserDetailAPi.as_view(),name = 'user-details')
]