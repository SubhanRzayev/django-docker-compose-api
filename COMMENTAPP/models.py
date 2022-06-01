from django.db import models
from django.contrib.auth.models import User
from POSTAPP.models import PostModel



# Create your models here.


class CommentModel(models.Model):
    #relation
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE,related_name='comments')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,blank=True,related_name='replies')
    
    
    comment_text = models.CharField(max_length=150,verbose_name="Comment text")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Comment time")
    modified_at = models.DateTimeField(auto_now=True,editable=False)
    
    
    class Meta:
        db_table = "Comments"
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
        ordering = ["created_at"]
        
        
    def __str__(self):
        return f"{self.author.username}"
    
    
    def children(self):
        return CommentModel.objects.filter(parent=self)
    
    
    @property
    def any_children(self):
        return CommentModel.objects.filter(parent=self).exists()
    

    


    