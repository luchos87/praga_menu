from cgitb import lookup
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import permissions

#-MENU----------------------------------------------------------

class MenuList(ListCreateAPIView):    
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()


class MenuDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Menu.objects.all()