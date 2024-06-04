from rest_framework.viewsets import ModelViewSet
from post.models import Post
from api.post.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer