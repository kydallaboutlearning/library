# utils/test_variables.py
"""Importinng Requiremensts"""
from django.utils import timezone
import datetime
from django.conf import settings
from accounts.models import CustomUser
from django.contrib.auth import get_user_model




"""Creating reusable test variables """


# setting up variables
t_title = "testtitle",
t_subtitle = "testSubtitle"
t_author = "testauthor"
t_isbn = "testisbn"
t_body = 'testbody'
t_time = timezone.now()
user = get_user_model()
t_username = 'testusername'
t_email = 'testemail@gmail.com'
t_password = 'testpassoword'
t_age = 19