from .models import Ejemplo
from rest_framework import viewsets, permissions
from .serializer import EjemploSerializer

class EjemploViewSet(viewsets.ModelViewSet):
    queryset = Ejemplo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EjemploSerializer