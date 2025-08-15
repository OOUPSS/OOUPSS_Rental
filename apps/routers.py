from django.urls import path, include


urlpatterns = [
    path('user/', include('apps.users.urls')),
    path('addresses/', include('apps.addresses.urls')),
    path('apartments/', include('apps.apartments.urls')),
    path('booking/', include('apps.booking.urls')),
    path('reviews/', include('apps.reviews.urls')),
]
