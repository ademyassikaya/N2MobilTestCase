from rest_framework.serializers import ModelSerializer
from album.models import Album


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ["user", "id", "title"]