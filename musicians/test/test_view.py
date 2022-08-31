from rest_framework.test import APITestCase

from albums.models import Album
from musicians.models import Musician
from songs.models import Song

class SongsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.musician_test = {
            "first_name": "freddie",
            "last_name": "mercury",
            "instrument": "vocal",
        }

        cls.album_musician = {"name": "albummm"}

        cls.song = {
            "name": "musiquinha",
            "duration": 356,
        }


        cls.musician_instance = Musician.objects.create(**cls.musician_test)

        cls.album_instance = Album.objects.create(
            **cls.album_musician, musician=cls.musician_instance
        )

        cls.song_instance = Song.objects.create(**cls.song, album=cls.album_instance)

    def test_song_create_(self):
        response = self.client.post(
            "/api/musicians/1/albums/1/songs/", self.song, format="json", follow=True
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], self.song["name"])
        self.assertEqual(response.data["duration"], self.song["duration"])
        self.assertEqual(response.data["album_id"], self.album_instance.id)
 

    def test_list_songs(self):
        response = self.client.get(
            "/api/musicians/1/albums/1/songs/", format="json", follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data["results"][0]["name"], self.song_instance.name
        )
        self.assertEqual(
            response.data["results"][0]["duration"], self.song_instance.duration
        )
        self.assertEqual(
            response.data["results"][0]["album_id"], self.song_instance.album_id
        )
        self.assertEqual(len(response.data["results"]), 1)