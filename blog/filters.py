import django_filters
from django_filters.widgets import RangeWidget

from .models import Flat


class FlatFilter(django_filters.rest_framework.FilterSet):
    price = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'text'}))
    square = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'text'}))

    class Meta:
        model = Flat
        fields = ['price', 'count_room', 'square']
