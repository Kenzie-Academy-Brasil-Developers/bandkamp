from django.shortcuts import get_object_or_404
from albums.models import Album
from albums.serializers import AlbumSerializer

from rest_framework.views import Response
from rest_framework import generics

from .models import Musician
from .serializers import MusicianSerializer, MusicianAlbumSerializer

class MusicianView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianAlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = MusicianAlbumSerializer

    def get(self, request, pk):
        musician = get_object_or_404(Musician, id=pk)

        albums = Album.objects.filter(musician=musician)

        serializer = AlbumSerializer(albums, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        return serializer.save(musician_id=self.kwargs["pk"])



