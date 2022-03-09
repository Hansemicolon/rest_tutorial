from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from django.http import JsonResponse
from .serializers import BoardSerializer
from rest_framework import generics
from .models import board
from rest_framework_simplejwt.authentication import JWTAuthentication

def viewjson(request):
    return JsonResponse("REST API end point...", safe=False)

@api_view(['GET'])
def index(request):
    # rest api의 엔드포인트!
    api_urls = {
        'List': 'boardlist',
        'Detail': 'boardview/<str:mbti>',
        'Create': 'boardinsert',
        'Update': 'boardupdate/<str:mbti>',
        'Delete': 'boarddelete/<str:mbti>',
    }

    return Response(api_urls)

@api_view(['GET'])
def boardList(request):
    # models
    boards = board.objects.all()
    serializer = BoardSerializer(boards, many=True)

    return Response(serializer.data)

@api_view(['PUT'])
def boardUpdate(request, user_name):
    boards = board.objects.get(user_name=user_name)
    serializer = BoardSerializer(instance=boards, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def boardInsert(request):
    #request.data안에는 json형태의 데이터가 들어있음
    # 직렬화 시켜서 저장
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

# 쿼리스트링 ->
class CustomBoardList(generics.ListAPIView):
    # 시리얼라이저
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # setting.py에 먼저 page size 정의해줌
    pagination_class = LargeResultsSetPagination
    # get_queryset사용으로 board모델 안에 있는거 다 갖고 와
    def get_queryset(self):
        input_params = {k: v for k, v in self.kwargs.items()}
        # TODO error handler
        input_val = input_params['mbti']
        qs = board.objects.filter(mbti=input_val)
        return qs
