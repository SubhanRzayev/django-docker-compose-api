from django.contrib import admin
from .models import CommentModel
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ["author","post","parent","comment_text","created_at"]
    
    
admin.site.register(CommentModel,CommentAdmin)

