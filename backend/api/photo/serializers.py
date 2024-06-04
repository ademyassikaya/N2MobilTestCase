from rest_framework.serializers import ModelSerializer
from photo.models import Photo


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ["album", "id", "title","url", "thumbnail_url"]