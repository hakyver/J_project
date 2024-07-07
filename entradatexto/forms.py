from django.forms import ModelForm
from .models import formulario

class formularioforms(ModelForm):
    class Meta:
        model = formulario
        fields = ['titulo', 'Comentario', 'Edad', 'Email', 'calificacion']