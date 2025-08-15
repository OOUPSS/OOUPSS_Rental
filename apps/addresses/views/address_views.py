from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.addresses.models.address_models import Address
from apps.addresses.serializers.address_serializers import AddressSerializer
from apps.users.permissions.landlord_permissions import IsLandlord


class AddressListCreateView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsLandlord]


class AddressDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsLandlord]