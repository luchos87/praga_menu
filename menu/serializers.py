from rest_framework.serializers import ModelSerializer
from .models import Menu
from rest_framework import serializers


class MenuSerializer(ModelSerializer):
    class Meta:
        model=Menu        

        fields=['id','imagen']