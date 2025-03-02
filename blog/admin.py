from django.contrib import admin
from .models import Post

# # Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
     class Meta:
          model = Post
          fields = "__all__"

     list_display = ['title', 'author','status', 'publish', 'created_at','updated_at']
     list_editable = ['status']
     search_fields = ['title', 'status', 'publish']  
     ordering = ['status', 'publish']
     show_facets = admin.ShowFacets.ALWAYS
    
     def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

