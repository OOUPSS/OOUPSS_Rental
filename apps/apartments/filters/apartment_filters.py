import django_filters
from apps.apartments.models.apartment_models import Apartment


class ApartmentFilter(django_filters.FilterSet):
    class Meta:
        model = Apartment
        fields = {
            'rooms': ['gte', 'lte'],
            'price': ['gte', 'lte'],
            'apartment_type': ['exact'],
            'address__city': ['exact', 'icontains'],
            'address__land': ['exact'],
        }
