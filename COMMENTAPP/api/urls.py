from django.urls import path
from .views import CommentListAPIView

app_name = 'comment'

urlpatterns = [
    path("list", CommentListAPIView.as_view(), name="list_comment"),
]
