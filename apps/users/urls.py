from django.urls import path
from apps.users.views.login_views import LoginAPIView
from apps.users.views.logout_views import LogoutUserAPIView
from apps.users.views.register_views import RegisterUserAPIView


urlpatterns = [
    path('sign-up/', RegisterUserAPIView.as_view()),
    path('sign-in/', LoginAPIView.as_view()),
    path('logout/', LogoutUserAPIView.as_view()),
]
