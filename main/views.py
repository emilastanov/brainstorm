from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class GetSameWordsView(APIView):
    def get(self, request, format=None):
        url = f'http://paraphraser.ru/api?token=b240acd79ee69718765e6f055b09aa7cc98c7f52&c=vector&lang=ru&query={request.GET.get("word")}&top=10&forms=0&scores=0'
        return Response(requests.get(url).json())
