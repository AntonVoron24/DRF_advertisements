from django_filters.rest_framework import FilterSet
from django_filters import DateFromToRangeFilter


from .models import Advertisement


class AdvertisementFilter(FilterSet):
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at', 'status', 'creator']

