from rest_framework import serializers
from .models import formulario
#cual es la funcion de un serializador?

class formularioserializer(serializers.ModelSerializer):
    class Meta:
        model = formulario
        fields=['id', 'nombre', 'fecha', 'Comentario', 'EDAD', 'Email', 'calificacion'] #los datos que pueden ser consultados
        read_only_fields= ('fecha',) #para que la fecha no pueda ser editada