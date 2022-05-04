from rest_framework.serializers import ModelSerializer
from .models import Encuesta

class EncuestaSerializer(ModelSerializer):
    class Meta:
        model=Encuesta        

        fields=['id','nombre','email','fecha_nac']