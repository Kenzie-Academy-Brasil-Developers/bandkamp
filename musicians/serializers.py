from django.shortcuts import get_object_or_404
from albums.models import Album
from albums.serializers import AlbumSerializer
from rest_framework import serializers

from .models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = Musician
        fields = ["id", "first_name", "last_name", "instrument", "albums"]
        

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)


