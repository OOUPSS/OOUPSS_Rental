from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request: Request, **kwargs):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if access_token:
            try:
                token = AccessToken(access_token)
                if datetime.fromtimestamp(token['exp']) < datetime.now():
                    raise TokenError('Token is expired')
                request.META['HTTP_AUTHORIZATION'] = f"Bearer {access_token}"

            except TokenError:
                new_access_token = self.refresh_access_token(refresh_token)

                if new_access_token:
                    request.META['HTTP_AUTHORIZATION'] = f"Bearer {new_access_token}"

                    request._new_access_token = new_access_token

                else:
                    self.clear_jwt_cookies(request)

        elif refresh_token:
            new_access_token = self.refresh_access_token(refresh_token)

            if new_access_token:
                request.META['HTTP_AUTHORIZATION'] = f"Bearer {new_access_token}"

                request._new_access_token = new_access_token

            else:
                self.clear_jwt_cookies(request)

    def process_response(self, request: Request, response: Response, **kwargs):
        new_access_token = getattr(request, '_new_access_token', None)

        if new_access_token:
            access_expiry = AccessToken(new_access_token)['exp']
            response.set_cookie(
                key='access_token',
                value=new_access_token,
                httponly=True,
                secure=False,
                samesite='Lax',
                expires=datetime.fromtimestamp(access_expiry)
            )
        return response

    def refresh_access_token(self, refresh_token):
        try:
            refresh = RefreshToken(refresh_token)
            new_access_token = str(refresh.access_token)

            return new_access_token
        except TokenError:
            return None

    def clear_jwt_cookies(self, request: Request):
        request.COOKIES.pop('access_token', None)
        request.COOKIES.pop('refresh_token', None)
