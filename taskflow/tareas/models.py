from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Etiqueta(models.Model):
    tipo = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.type

class Tarea(models.Model):
    STATUS_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('En progreso', 'En progreso'),
    ('Completada', 'Completada'),
    ]
        
    titulo = models.CharField(max_length=50, blank=False, null=False)
    fecha = models.DateField()
    descripcion = models.CharField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pendiente')
    tareas_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tareas_etiqueta = models.ForeignKey(Etiqueta, default=1, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.titulo} > {self.tareas_owner}'

