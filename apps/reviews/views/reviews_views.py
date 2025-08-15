from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import SAFE_METHODS, AllowAny
from apps.reviews.models.reviews_models import Review
from apps.reviews.serializers.reviews_serializers import ReviewSerializer
from apps.users.permissions.renter_permissions import IsRenter, IsRenterOwner


class ReviewListCreateView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsRenter]

        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        return serializer.save(renter=self.request.user)


class ReviewDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsRenterOwner]

        return [permission() for permission in self.permission_classes]