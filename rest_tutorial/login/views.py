from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import LoginSerializer


# Create your views here.


class LoginView(CreateAPIView):
    model = User
    serializer_class = LoginSerializer

    def get_queryset(self):
        return User.objects.all()
