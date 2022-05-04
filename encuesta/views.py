from cgitb import lookup
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Encuesta
from .serializers import EncuestaSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class EncuestaList(ListCreateAPIView):    
    serializer_class = EncuestaSerializer

    def post(self, request):
        data  = request.data
        email = data.get('email','')

        serializer = EncuestaSerializer(data=request.data)

        if not Encuesta.objects.filter(email=email).exists():
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail':'El mail ya esta registrado'}, status=status.HTTP_400_BAD_REQUEST)


    def get_queryset(self):
        return Encuesta.objects.all()

class EncuestaDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EncuestaSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Encuesta.objects.all()
