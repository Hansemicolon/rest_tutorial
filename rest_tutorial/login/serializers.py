from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'password'
        ]


class CustomTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        # user는 입력한 username임 ->semi
        print(user)
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        # OrderedDict([('username', 'semi'), ('password', 'tpaltpal')])
        # username : semi,
        # password : tpaltpal
        # 가 들어있음
        data = super().validate(attrs)
        # data 안에는 refresh과 access 토큰이 딕셔너리 형태로 들어있음

        refresh = self.get_token(self.user)

        # data json안에 refresh와 access와 username을 넣어서 반환함
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = str(self.user.username)
        return data
