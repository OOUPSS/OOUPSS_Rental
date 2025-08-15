from datetime import timedelta
from rest_framework import serializers
from apps.apartments.models.apartment_models import Apartment
from apps.apartments.serializers.apartment_serializers import ApartmentSerializer
from apps.booking.models.booking_models import Booking
from django.utils import timezone
from django.db.models import Q


def check_dates_availability(apartment, date_from, date_to, booking_id=None):
    overlapping_reservations = Booking.objects.filter(
        apartment=apartment,
        is_canceled=False,
        is_approved_by_landlord=True,
    ).exclude(id=booking_id).filter(
        Q(date_from__lte=date_to) & Q(date_to__gte=date_from)
    )

    if overlapping_reservations.exists():
        raise serializers.ValidationError(
            'The apartment is already reserved for the selected dates.'
        )


class BookingSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['renter', 'apartment', 'date_from', 'date_to', 'is_approved_by_landlord', 'is_canceled']
        read_only_fields = ['renter', 'is_canceled']


class BookingCreateSerializer(serializers.ModelSerializer):
    apartment = serializers.PrimaryKeyRelatedField(
        queryset=Apartment.objects.filter(is_active=True),
        write_only=True
    )
    apartment_details = ApartmentSerializer(read_only=True, source='apartment')

    class Meta:
        model = Booking
        fields = [
            'renter',
            'apartment',
            'apartment_details',
            'date_from',
            'date_to',
            'is_approved_by_landlord',
            'is_canceled',
        ]
        read_only_fields = ['renter', 'is_approved_by_landlord', 'is_canceled']

    def validate(self, data):
        date_from = data.get('date_from')
        date_to = data.get('date_to')
        apartment = data.get('apartment')
        renter = self.context['request'].user

        if apartment.landlord == renter:
            raise serializers.ValidationError('You cannot book your own apartment.')

        if date_from >= date_to:
            raise serializers.ValidationError('Date From must be earlier than Date To.')

        check_dates_availability(apartment, date_from, date_to)

        if date_from < timezone.now().date():
            raise serializers.ValidationError('Date From must be today or later.')

        if date_to < timezone.now().date() + timedelta(days=1):
            raise serializers.ValidationError('Date To must be tomorrow or later.')

        return data


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'apartment',
            'date_from',
            'date_to',
            'is_approved_by_landlord',
            'is_canceled',
        ]
        read_only_fields = ['is_canceled', 'is_approved_by_landlord']

    def validate(self, data):
        date_from = data.get('date_from', self.instance.date_from)
        date_to = data.get('date_to', self.instance.date_to)
        apartment = data.get('apartment', self.instance.apartment)

        if date_from >= date_to:
            raise serializers.ValidationError('Date From must be earlier than Date To.')
        
        if date_from < timezone.now().date():
            raise serializers.ValidationError('Date From must be today or later.')
        
        if date_to < timezone.now().date() + timedelta(days=1):
            raise serializers.ValidationError('Date To must be tomorrow or later.')

        check_dates_availability(apartment, date_from, date_to, self.instance.id)

        return data


class CancelBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['is_canceled']
        read_only_fields = [
            'renter',
            'apartment',
            'date_from',
            'date_to',
            'is_approved_by_landlord',
        ]

    def validate_is_canceled(self, value):
        if self.instance.is_approved_by_landlord:
            raise serializers.ValidationError('Cannot cancel an approved booking.')
        if self.instance.is_canceled:
            raise serializers.ValidationError('Booking is already canceled.')
        
        date_from = self.instance.date_from
        
        if value and timezone.now().date() >= date_from - timedelta(days=3):
            raise serializers.ValidationError(
                "You can cancel your booking up to 3 days in advance."
            )
        return value


class ApproveBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['is_approved_by_landlord']
        read_only_fields = [
            'renter',
            'apartment',
            'date_from',
            'date_to',
            'is_canceled',
        ]

    def validate_is_approved_by_landlord(self, value):
        if self.instance.is_approved_by_landlord:
            raise serializers.ValidationError('Booking is already approved.')
        if self.instance.is_canceled:
            raise serializers.ValidationError('Cannot approve a canceled booking.')
        return value