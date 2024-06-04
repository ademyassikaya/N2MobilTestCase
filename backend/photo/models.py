from django.db import models
from album.models import Album

class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    thumbnail_url = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
