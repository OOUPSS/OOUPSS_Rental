from rest_framework.permissions import BasePermission


class IsRenter(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and not request.user.is_landlord
            and not request.user.is_staff
        )


class IsRenterOwner(IsRenter):
    def has_object_permission(self, request, view, obj):
        return obj.renter == request.user
