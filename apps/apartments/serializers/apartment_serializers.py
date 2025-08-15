from django.db import IntegrityError
from rest_framework import serializers
from apps.addresses.models.address_models import Address
from apps.addresses.serializers.address_serializers import ApartmentAddressSerializer
from apps.apartments.models.apartment_models import Apartment
from apps.reviews.serializers.reviews_serializers import ApartmentReviewSerializer


def get_or_create_address(address_data):
    address, created = Address.objects.get_or_create(
        land=address_data['land'],
        city=address_data['city'],
        street=address_data['street'],
        house_number=address_data['house_number'],
        postal_code=address_data['postal_code']
    )
    return address


class ApartmentSerializer(serializers.ModelSerializer):
    address = ApartmentAddressSerializer()
    reviews = ApartmentReviewSerializer(many=True, read_only=True)
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = ['landlord', 'reviews', 'avg_rate']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = get_or_create_address(address_data)
        try:
            apartment = Apartment.objects.create(address=address, **validated_data)
        except IntegrityError:
            raise serializers.ValidationError("This combination of title and address already exists.")

        return apartment

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address = get_or_create_address(address_data)
            instance.address = address

        for key, value in validated_data.items():
            setattr(instance, key, value)

        try:
            instance.save()
        except IntegrityError:
            raise serializers.ValidationError("This combination of title and address already exists.")

        return instance

    def get_avg_rate(self, obj):
        return obj.avg_rate
