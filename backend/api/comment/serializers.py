from rest_framework.serializers import ModelSerializer
from comment.models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # TODO: post -> postId olmali
        fields = ["post_id","post","id", "name", "body"]
        extra_kwargs = {
            "post_id": {"read_only": True},
            "post": {"write_only": True},
        }