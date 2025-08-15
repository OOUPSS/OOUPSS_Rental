from django.db import models
from apps.apartments.models.apartment_models import Apartment
from apps.users.models.user_models import User


class Booking(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='bookings')
    date_from = models.DateField()
    date_to = models.DateField()
    is_approved_by_landlord = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

