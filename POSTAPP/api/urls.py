from django.urls import path
from .views import PostCreateAPIView, PostDeleteAPIView, PostDetailAPIView, PostListAPIView

app_name="post"

urlpatterns = [
    path("list/",PostListAPIView.as_view(),name="postList"),
    path("detail/<slug>",PostDetailAPIView.as_view(),name="postDetail"),
    path("delete/<slug>", PostDeleteAPIView.as_view(),name="postDelete"),
    path("create/", PostCreateAPIView.as_view(), name="postCreate"),

]