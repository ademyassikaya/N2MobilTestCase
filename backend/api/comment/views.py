from rest_framework.viewsets import ModelViewSet
from comment.models import Comment
from api.comment.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer