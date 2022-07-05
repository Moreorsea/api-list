import django_filters

from .models import Flat


class FlatFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = Flat
        fields = ['price', 'count_room', 'square']
