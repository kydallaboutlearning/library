from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser
from .forms import CustomuUserCreationForm, CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
     add_form = CustomuUserCreationForm
     form = CustomUserChangeForm
     model = CustomUser
     list_display = [
          'email',
          'username',
          'age',
          'is_staff',
     ]

     fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
     add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)



# registering them
admin.site.register(CustomUser, CustomUserAdmin)
