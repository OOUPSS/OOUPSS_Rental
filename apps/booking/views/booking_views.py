from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import SAFE_METHODS
from apps.booking.models.booking_models import Booking
from apps.booking.serializers.booking_serializers import (
    BookingCreateSerializer,
    BookingSerializer,
    BookingDetailsSerializer,
    CancelBookingSerializer,
    ApproveBookingSerializer,
)
from apps.users.permissions.landlord_permissions import IsLandlordOwnerOfReservationApartment, IsLandlord
from apps.users.permissions.renter_permissions import IsRenterOwner, IsRenter
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


class BookingListCreateView(ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        return BookingSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()

        user = self.request.user
        if user.is_landlord:
            return Booking.objects.filter(apartment__landlord=user).order_by('date_from')
        else:
            return Booking.objects.filter(renter=user).order_by('date_from')

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsRenter | IsLandlord]
        else:
            self.permission_classes = [IsRenter]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(renter=self.request.user)


class BookingDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailsSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [IsRenterOwner | IsLandlordOwnerOfReservationApartment]
        else:
            self.permission_classes = [IsRenterOwner]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Booking.objects.none()

        user = self.request.user
        return Booking.objects.filter(Q(renter=user) | Q(apartment__landlord=user))

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class BookingCancelView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = CancelBookingSerializer
    permission_classes = [IsRenterOwner]
    lookup_field = 'pk'
    http_method_names = ['patch']

    def perform_update(self, serializer):
        serializer.save(is_canceled=True)


class BookingApproveView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = ApproveBookingSerializer
    permission_classes = [IsLandlordOwnerOfReservationApartment]
    lookup_field = 'pk'
    http_method_names = ['patch']

    def perform_update(self, serializer):
        serializer.save(is_approved_by_landlord=True)