from django.shortcuts import render

from .models import Song

# Create your views here.


def index_view(request):
    songs = Song.objects.all()
    count = range(1, 13)
    print(songs)
    print("*" * 50)
    context = {"songs": songs, "count": count}
    return render(request, "music/index.html", context)
