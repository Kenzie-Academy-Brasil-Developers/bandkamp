from django.shortcuts import get_object_or_404
from django.db.models import Sum

from albums.models import Album
from albums.serializers import AlbumSerializer
from songs.models import Song
from songs.serializers import SongSerializer

from rest_framework.views import Response
from rest_framework import generics

from .models import Musician
from .serializers import MusicianSerializer

class MusicianView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianAlbumView(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])
        
        serializer.save(musician=musician)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs['pk'])

        return Album.objects.filter(musician=musician).order_by("id")


class MusicianAlbumSongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        musician = get_object_or_404(Musician, pk=self.kwargs["pk"])
        album = get_object_or_404(Album, pk=self.kwargs['album_id'])
        
        serializer.save(album=album)

    def get_queryset(self):
        musician = get_object_or_404(Musician, pk=self.kwargs["pk"])
        album = get_object_or_404(Album, pk=self.kwargs['album_id'])

        songs = Song.objects.filter(album=album)

        return songs.order_by("id")
