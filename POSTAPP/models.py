from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.utils.text import slugify

from django.db import models

# Create your models here.

class PostModel(models.Model):
    author       = models.ForeignKey(User,on_delete=models.CASCADE)
    title        = models.CharField(max_length=50)
    content      = models.TextField()
    draft        = models.BooleanField(default=False)
    createdDate  = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    slug          =AutoSlugField(unique=True,editable=False,populate_from="Title")
    image        = models.ImageField(upload_to="PostImages",null=True,blank=True)
    
    
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            return super(PostModel,self).save(*args,**kwargs)
        
        
    class Meta:
        db_table="Posts"
        verbose_name_plural="Postlar"
        verbose_name="Post"
        
        
    def __str__(self):
        return self.title