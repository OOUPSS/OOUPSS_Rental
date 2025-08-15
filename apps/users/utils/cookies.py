from datetime import datetime
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


def set_jwt_cookies(response: Response, user) -> Response:
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token

    access_expiry = datetime.fromtimestamp(access_token['exp'])
    refresh_expiry = datetime.fromtimestamp(refresh_token['exp'])

    response.set_cookie(
        key='access_token',
        value=str(access_token),
        httponly=True,
        secure=False,
        samesite='Lax',
        expires=access_expiry
    )
    response.set_cookie(
        key='refresh_token',
        value=str(refresh_token),
        httponly=True,
        secure=False,
        samesite='Lax',
        expires=refresh_expiry
    )

    return response