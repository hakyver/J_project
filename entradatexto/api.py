from .models import formulario
from rest_framework import viewsets, permissions
from .serializers import formularioserializer

class userViewSet (viewsets.ModelViewSet):
    queryset = formulario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = formularioserializer