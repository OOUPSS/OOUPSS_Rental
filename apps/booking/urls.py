from django.urls import path
from apps.booking.models.booking_models import Booking
from apps.booking.views.booking_views import BookingListCreateView, BookingDetailUpdateDeleteView
from apps.booking.views.booking_views import BookingCancelView, BookingApproveView



urlpatterns = [
    path("", BookingListCreateView.as_view()),
    path("<int:pk>/", BookingDetailUpdateDeleteView.as_view()),
    path("<int:pk>/approve/", BookingApproveView.as_view()),
    path("<int:pk>/cancel/", BookingCancelView.as_view()),
]
