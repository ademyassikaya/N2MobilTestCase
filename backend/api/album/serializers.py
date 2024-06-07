from rest_framework.serializers import ModelSerializer
from album.models import Album


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ["user_id","user", "id", "title"]
        extra_kwargs = {
            "user_id": {"read_only": True},
            "user": {"write_only": True},
        }