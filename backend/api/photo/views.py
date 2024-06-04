from rest_framework.viewsets import ModelViewSet
from photo.models import Photo
from api.photo.serializers import PhotoSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer