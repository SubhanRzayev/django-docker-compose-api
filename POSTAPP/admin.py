from django.contrib import admin

from POSTAPP.models import PostModel

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["author","title","content","slug","createdDate","modifiedDate"]
    
    
admin.site.register(PostModel,PostAdmin)


