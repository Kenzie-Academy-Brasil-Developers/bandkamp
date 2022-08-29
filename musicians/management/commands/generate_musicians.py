from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from musicians.models import Musician
from albums.models import Album

class Command(BaseCommand):
    help = 'create random musicians'

    def handle(self, *args, **options):
        for i in range(2):
            Musician.objects.create(
                first_name=get_random_string(5),
                last_name=get_random_string(5),
                instrument=get_random_string(10),
            )

        musician = Musician.objects.all()
        for i in range(2):
            Album.objects.create(name=get_random_string(5), musician=musician[i])