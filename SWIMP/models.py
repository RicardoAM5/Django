from django.db import models

# Create your models here.

class Ejemplo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    numero = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)