from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS, AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.apartments.filters.apartment_filters import ApartmentFilter
from apps.apartments.models.apartment_models import Apartment
from apps.apartments.serializers.apartment_serializers import ApartmentSerializer
from apps.users.permissions.landlord_permissions import IsLandlord, IsLandlordOwner
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class ApartmentViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ApartmentFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsLandlord, IsLandlordOwner]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(landlord=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_landlord:
            return Apartment.objects.all()
        else:
            return Apartment.objects.filter(is_active=True)

    def get_object(self):
        obj = get_object_or_404(Apartment, pk=self.kwargs['pk'])
        if not obj.is_active and not self.request.user.is_landlord:
            raise NotFound()
        self.check_object_permissions(self.request, obj)
        return obj

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('rooms__gte', openapi.IN_QUERY, description="Filter by min rooms", type=openapi.TYPE_NUMBER),
            openapi.Parameter('rooms__lte', openapi.IN_QUERY, description="Filter by max rooms", type=openapi.TYPE_NUMBER),
            openapi.Parameter('price__gte', openapi.IN_QUERY, description="Filter by min price", type=openapi.TYPE_NUMBER),
            openapi.Parameter('price__lte', openapi.IN_QUERY, description="Filter by max price", type=openapi.TYPE_NUMBER),
            openapi.Parameter('apartment_type', openapi.IN_QUERY, description="Filter by apartment type", type=openapi.TYPE_STRING),
            openapi.Parameter('address__city', openapi.IN_QUERY, description="Filter by city", type=openapi.TYPE_STRING),
            openapi.Parameter('address__land', openapi.IN_QUERY, description="Filter by land", type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)