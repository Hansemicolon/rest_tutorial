from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from django.http import JsonResponse
from .serializers import BoardSerializer
from .models import board

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

@api_view(['GET'])
def boardView(request, mbti):
    boards = board.objects.filter(mbti=mbti)
    serializer = BoardSerializer(boards, many=True)

    return Response(serializer.data)