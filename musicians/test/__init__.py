from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from musicians.models import Musician
from albums.models import Album
from songs.models import Song


class ProductViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        ...
