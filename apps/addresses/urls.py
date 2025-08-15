from django.urls import path

from apps.addresses.views.address_views import AddressListCreateView, AddressDetailUpdateDeleteView


urlpatterns = [
    path("", AddressListCreateView.as_view()),
    path("<int:pk>/", AddressDetailUpdateDeleteView.as_view()),
]
