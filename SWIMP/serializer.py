from rest_framework import serializers

from .models import Ejemplo

class EjemploSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejemplo
        fields = '__all__'
        read_only_fields = ['created',]