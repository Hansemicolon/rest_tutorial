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
# bert?
# 코벌트? 벌트를 만ㄷ름?
# 뭔소리임?
# postgre sql 만들면 데이터 밀어 넣기
# 인덱스 설계 ->
# 각자 수집한 데이타로 es인덱스 구성하기 -> 제이 블로그 중에 노리 필터 -> 명사만 추출 -> 에널라이저 붙여서 인덱스 구정
# 키바나 준비되어있으니까 한번 보여주기 (198.2??????)
# mbti만 우선 인덱스에 넣어놓고
# 노리가 매캅 -> 사용자 사전 편집 가능? -> 할 수 있는데 되게 안좋음
# 유저딕트 조사해오기 -> 실제 추가 하는 방법
# 필터로 게시물에서 노리로 발라지고 -> 필드에 넣어서 실제로 검색할 수 있게
# 인프제,,, 인팁,,, intp,,,아이엔티피