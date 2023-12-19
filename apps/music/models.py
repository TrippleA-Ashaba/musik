from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to="artist/", blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    class GenreChoices(models.TextChoices):
        ROCK = ("rock",)
        POP = "pop"
        JAZZ = "jazz"
        COUNTRY = "country"
        FOLK = "folk"
        ELECTRONIC = "electronic"
        HIP_HOP = "hip hop"
        BLUES = "blues"
        CLASSICAL = "classical"
        REGGAE = "reggae"
        METAL = "metal"
        PUNK = "punk"
        FUNK = "funk"
        SOUL = "soul"
        RNB = "r&b"
        DISCO = "disco"
        HOUSE = "house"
        TECHNO = "techno"
        TRANCE = "trance"
        DANCE = "dance"
        DUBSTEP = "dubstep"
        DUB = "dub"
        AMBIENT = "ambient"
        LOUNGE = "lounge"
        INDIE = "Indie"
        ALTERNATIVE = "alternative"
        OTHER = "other"

    name = models.CharField(max_length=100, choices=GenreChoices.choices, default=GenreChoices.OTHER)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to="albums/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to="songs/", blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.song_title} - {self.artist}"
