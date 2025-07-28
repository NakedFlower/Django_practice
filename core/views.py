from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Place
from .serializers import PlaceSerializer
from rest_framework import viewsets

class PlaceList(APIView):
    def get(self, request):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer