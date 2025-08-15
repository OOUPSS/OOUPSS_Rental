from enum import Enum


class ApartmentTypes(Enum):
    HOTEL = "Hotel"
    HOUSE = "House"
    APARTMENT = "Apartment"
    STUDIO = "Studio"
    HOSTEL = "Hostel"
    PENTHOUSE = "Penthouse"
    FLAT = "Flat"

    @classmethod
    def choices(cls):
        return [(attr.value, attr.value) for attr in cls]
