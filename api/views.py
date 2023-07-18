from django.shortcuts import render
from .translator import OriginalTranslator, GenerateProductDescription
from .imagegenerator import imageGenerator
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TranslatorSerializer, DescriptionSerializer, ImageSerializer


# Create your views here.

class TranslatorView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = TranslatorSerializer(data=request.data)
        if serializer.is_valid():
            target = serializer.data['language']['value']
            text = serializer.data['description']
            
            result = OriginalTranslator(target, text)
            return Response({
                "status": "success",
                "data": result
            }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class DescriptionView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = DescriptionSerializer(data=request.data)

        if serializer.is_valid():
            title = serializer.data['title']
            information = serializer.data['information']
            keywords = serializer.data['keywords']
            number = serializer.data['number']

            info = {
                'title': title,
                'information': information,
                'keywords': keywords,
                'number': number
            }

            result = GenerateProductDescription(info)
            return Response({
                'status': 'success',
                'data': result
            }, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class ImageGenerationView(APIView):
    http_method_names = ['post']

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        
        if serializer.is_valid():
            title = serializer.data['title']
            topic = serializer.data['topic']
            effect = serializer.data['effect']
            perspective = serializer.data['perspective']

            info = {
                'Title': title,
                'Topic': topic['value'],
                'Effect': effect['value'],
                'Perspective': perspective['value']
            }
            url = imageGenerator(info)

            return Response({
                'status': 'success',
                'data': url
            }, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
