from rest_framework.serializers import ModelSerializer
from post.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["user_id", "user", "id", "title", "body"]
        extra_kwargs = {
            "user_id": {"read_only": True},
            "user": {"write_only": True},
        }