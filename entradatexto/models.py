from django.db import models

# Create your models here.
class formulario(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField(auto_now_add=True, blank=True)
    Comentario=models.TextField(max_length=500)
    EDAD=models.TextField(max_length=3)
    Email=models.EmailField(max_length=500)
    calificacion = models.IntegerField(default=0)

    class Meta:
        db_table = 'formulario'