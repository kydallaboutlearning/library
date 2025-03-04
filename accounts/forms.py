from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser



# seting up the forms

class CustomUserCreationForm(UserCreationForm):
     class Meta(UserCreationForm):
          model = CustomUser
          fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm):
     class Meta(UserCreationForm):
          model = CustomUser
          fields = UserChangeForm.Meta.fields
