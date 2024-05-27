from django.shortcuts import render
from rest_framework import viewsets
from .serializers import formularioserializer
from .models import formulario
from django.http.response import JsonResponse

#aqui defines los html que vas a utilizar 
# Create your views here.
def index (request):
    return render(request,'index.html')
def comentariosview (request):
    return render(request,'comentarios_list.html')
    
class formularioViewSet(viewsets.ModelViewSet):
    queryset=formulario.objects.all()
    serializer_class=formularioserializer
def listacomentarios(request):
    comentarios_list = list(formulario.objects.values())
    data = {'comentarios': comentarios_list}
    return JsonResponse(data)
