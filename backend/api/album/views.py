from rest_framework.viewsets import ModelViewSet
from album.models import Album
from api.album.serializers import AlbumSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer