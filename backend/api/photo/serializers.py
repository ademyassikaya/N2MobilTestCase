from rest_framework.serializers import ModelSerializer
from photo.models import Photo


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ["album_id","album", "id", "title","url", "thumbnail_url"]
        extra_kwargs = {
            "album_id": {"read_only": True},
            "album": {"write_only": True},
        }