from django.db import models
from django.contrib.auth.models import User

class formulario(models.Model):
    titulo = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    Comentario = models.TextField(max_length=500)
    Edad = models.TextField(max_length=3)
    Email = models.EmailField(max_length=500)
    calificacion = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'formulario'
    
    def __str__(self):
        return self.nombre