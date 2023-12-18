from django.db import models


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.artist}"


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.song_title} - {self.album.artist}"
