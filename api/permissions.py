"""Creating permissions for the api"""
# importing requirements
from rest_framework import permissions

# defining the permissions
class IsAdminUserorReadOnly(permissions.BasePermission):
     def has_permission(self, request, view):
          # only authenticated user can access the list view
          if request.user.is_authenticated:
               return True
          
          return False

     # only the writer can edit the post
     def has_object_permission(self, request, view, obj):
          if request.method in permissions.SAFE_METHODS:
               return True
          # writing permissions is only allowed for the authors
          return obj.author == request.user

