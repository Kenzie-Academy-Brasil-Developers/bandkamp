from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.Serializer):
    class Meta:
        model = Album
        fields = ["id", "name", "musician_id"]

    def create(self, validated_data):
        return Album.objects.create(**validated_data)
