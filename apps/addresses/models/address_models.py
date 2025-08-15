import re
from django.db import models
from django.core.exceptions import ValidationError
from apps.choices import Lands


def validate_postal_code(value):
    if not re.match(r'^[0-9]{5}$', value):
        raise ValidationError(
            f'{value} is not a valid German postal code format. Postal code should be between 01001 and 99998.'
        )
    if int(value) < 1001 or int(value) > 99998:
        raise ValidationError(
            f'{value} is not a valid German postal code range. Postal code should be between 01001 and 99998.'
        )


class Address(models.Model):
    land = models.CharField(max_length=25, choices=Lands.choices)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=5, validators=[validate_postal_code])