from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.booking.models.booking_models import Booking
from apps.users.models.user_models import User


class Review(models.Model):
    renter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    rate = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Rate must be between 1 and 5.'
    )
    reservation = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='review')