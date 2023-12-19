from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    photo = models.ImageField(upload_to="artist/", blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.photo.delete(save=False)  # delete file from local storage
        super().delete(*args, **kwargs)  # delete Artist instance


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    year = models.IntegerField(blank=True, null=True)
    cover = models.ImageField(upload_to="albums/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("title", "artist")

    def __str__(self):
        return f"{self.title} - {self.artist}"

    def delete(self, *args, **kwargs):
        self.cover.delete(save=False)  # delete file from local storage
        super().delete(*args, **kwargs)  # delete Album instance


class Genre(models.Model):
    class GenreChoices(models.TextChoices):
        ROCK = "rock"
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

    name = models.CharField(max_length=100, choices=GenreChoices.choices, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True, related_name="songs")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="songs")
    genre = models.ManyToManyField(Genre, related_name="songs")
    file = models.FileField(
        upload_to="songs/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["mp3", "wav"])],
        help_text="Allowed formats: .mp3, .wav",
    )
    duration = models.IntegerField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ("title", "artist", "album")

    def __str__(self):
        return f"{self.title} - {self.artist}"

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)  # delete file from local storage
        super().delete(*args, **kwargs)  # delete Song instance


@receiver(post_delete, sender=Artist)
def delete_artist_files(sender, instance, **kwargs):
    instance.photo.delete(save=False)


@receiver(post_delete, sender=Album)
def delete_album_files(sender, instance, **kwargs):
    instance.cover.delete(save=False)


@receiver(post_delete, sender=Song)
def delete_song_files(sender, instance, **kwargs):
    instance.file.delete(save=False)
