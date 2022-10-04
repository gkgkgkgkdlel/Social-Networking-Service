from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import UserSerializer
import json
import bcrypt
import re
from .models import User


@permission_classes((AllowAny,))
class SignupView(APIView):
    def post(self, request):
        """
        회원가입 api.
        """
        email = request.data["email"]
        password = request.data["password"]
        name = request.data["name"]

        user = User.objects.create_user(
            email=email, password=password, name=name
        )

        user.save()

        token = Token.objects.create(user=user)

        return Response({"Token": token.key})


@permission_classes((AllowAny,))
class LoginView(APIView):
    def post(self, request):
        """
        로그인 api.
        """
        email = request.data.get("email")
        password = request.data.get("password")

        if email is None or password is None:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 여기서 authenticate로 유저 validate
        user = authenticate(request, email=email, password=password)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # user 로 토큰 발행
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)
