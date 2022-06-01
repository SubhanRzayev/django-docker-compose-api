
from rest_framework import serializers
from datetime import datetime

from POSTAPP.models import PostModel
from COMMENTAPP.api.serializers import CommentListSerializers

class PostSerializer(serializers.ModelSerializer):
    
    author = serializers.SerializerMethodField(method_name="get_Author")
    
    createdDate  = serializers.SerializerMethodField(method_name="get_CreatedDate")
    modifiedDate = serializers.SerializerMethodField(method_name="get_ModifiedDate")
    
            
    def get_Author(self,obj):
        return obj.Author.username
        
    def get_CreatedDate(self,obj):
        today = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return str(today)
    
    def get_ModifiedDate(self,obj):
        today = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return str(today)

    
    def get_Author(self,obj):
        return obj.author.username
    
    class Meta:
        model  = PostModel
        fields =  ["author","title","content",'draft','createdDate','modifiedDate']
        

class PostDetailSerializer(serializers.ModelSerializer):
    author      = serializers.SerializerMethodField(method_name="get_Author")

    
    
    comments    = serializers.SerializerMethodField(method_name="get_Yorumlar")

    def get_Yorumlar(self,obj):
        comments   = obj.comments.filter(parent=None)
        serializer = CommentListSerializers(comments,many=True)
        if serializer.data==[]:
            return None
        return serializer.data

    
    def get_Author(self,obj):
        return obj.author.username
    
    
    class Meta:
        model  = PostModel
        fields =["author","title","content","comments",'draft','image']
        
        
class PostCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["title","content",'draft','image']