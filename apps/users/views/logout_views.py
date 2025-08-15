from django.contrib.auth import logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class LogoutUserAPIView(APIView):
    def post(self, request: Request):
        if request.user:
            logout(request)

        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response
