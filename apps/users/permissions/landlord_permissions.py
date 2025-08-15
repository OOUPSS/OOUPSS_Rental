from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsLandlord(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_landlord)


class IsLandlordOwner(IsLandlord):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.landlord == request.user


class IsLandlordOwnerOfReservationApartment(IsLandlord):
    def has_object_permission(self, request, view, obj):
        return obj.apartment.landlord == request.user
