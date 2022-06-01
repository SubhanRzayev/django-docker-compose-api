
from POSTAPP.api.paginations import PostPagination
from POSTAPP.api.permissions import IsOwner
from POSTAPP.api.serializers import PostCreateUpdateSerializer, PostDetailSerializer, PostSerializer
from POSTAPP.models import PostModel
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = PostModel.objects.filter(draft=False)
        return queryset
    
    
    
class PostDetailAPIView(RetrieveAPIView):
    queryset         = PostModel.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field     = 'slug'


class PostDeleteAPIView(DestroyAPIView):
    queryset           = PostModel.objects.all()
    serializer_class   = PostSerializer
    permission_classes = [IsOwner,IsAuthenticated]
    lookup_field       = 'slug'




class PostCreateAPIView(CreateAPIView):
    queryset           = PostModel.objects.all()
    serializer_class   = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(Author=self.request.user)
