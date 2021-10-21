import django_filters

from .models import *


class DietaryItemFilter(django_filters.FilterSet):
    order__title = django_filters.CharFilter(lookup_expr='icontains')
    order__category = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        dietary_item = DietaryItem
        fields = ['title', 'category']
