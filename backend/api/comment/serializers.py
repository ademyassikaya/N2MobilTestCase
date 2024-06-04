from rest_framework.serializers import ModelSerializer
from comment.models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # TODO: post -> postId olmali
        fields = ["post", "name", "body"]