from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import CommentModel


class CommentListSerializers(ModelSerializer):

    replies = serializers.SerializerMethodField(method_name="get_replies")
    author = serializers.SerializerMethodField(method_name="get_author")
    
    
    def get_replies(self,obj):
        if obj.any_children:
            return CommentListSerializers(obj.children(),many=True).data
            

    
    def get_author(self,obj):
        return obj.author.username    

    
    class Meta:
        model = CommentModel
        fields = ["author","post","parent","comment_text","replies","created_at","modified_at"]