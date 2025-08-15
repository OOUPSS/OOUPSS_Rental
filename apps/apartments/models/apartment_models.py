from django.db import models
from apps.addresses.models.address_models import Address
from apps.choices.type_apartment import ApartmentTypes
from apps.users.models.user_models import User


class Apartment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    landlord = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='apartments'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        related_name='apartments',
        null=True,
        blank=True
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rooms = models.SmallIntegerField()
    apartment_type = models.CharField(max_length=20, choices=ApartmentTypes.choices, default=ApartmentTypes.APARTMENT)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'address')

    @property
    def avg_rate(self):
        reviews = self.reviews
        if reviews:
            avg_rate = sum(review.rate for review in reviews) / len(reviews)
            return round(avg_rate, 1)
        return 0

    @property
    def reviews(self):
        return [booking.review for booking in self.bookings.all() if hasattr(booking, 'review')]

    def __str__(self):
        return self.title
