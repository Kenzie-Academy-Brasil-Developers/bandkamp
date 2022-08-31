from django_filters import rest_framework as filters

from songs.models import Song

class SongFilter(filters.FilterSet):
    max_duration = filters.NumberFilter(field_name="duration", lookup_expr="lte")
    min_duration = filters.NumberFilter(field_name="duration", lookup_expr="gte")
    
    class Meta:
        model = Song
        fields = ["name"]