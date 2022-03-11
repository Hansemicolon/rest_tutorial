from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer, CustomTokenPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.


class SignupView(CreateAPIView):
    model = User
    authentication_classes = (TokenAuthentication, )
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

class CustomTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer

