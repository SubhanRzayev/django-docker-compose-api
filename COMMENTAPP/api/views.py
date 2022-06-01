from django import views
from rest_framework.generics import ListAPIView
from .serializers import CommentListSerializers
from .paginations import CommentPagination
from ..models import CommentModel


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializers
    pagination_class = CommentPagination
    
    
    def get_queryset(self):
        queryset = CommentModel.objects.filter(parent=None)
        return queryset
    
    

    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    