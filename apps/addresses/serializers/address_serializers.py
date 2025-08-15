from rest_framework import serializers
from apps.addresses.models.address_models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def validate(self, data):
        try:
            Address.objects.get(**data)
            raise serializers.ValidationError('Address already exists')
        except Address.DoesNotExist:
            return data


class ApartmentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
