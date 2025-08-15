from rest_framework.routers import DefaultRouter
from apps.apartments.views.apartments_views import ApartmentViewSet

router = DefaultRouter()
router.register('', ApartmentViewSet, basename='apartments')

urlpatterns = router.urls