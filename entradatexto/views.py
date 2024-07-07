from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import formulario
from .forms import formularioforms

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'GET':
        return render(request, 'entradatexto/index.html', {'form': UserCreationForm()})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'entradatexto/index.html', {'form': UserCreationForm()})

def loginView(request):
    if request.method == 'GET':
        return render(request, 'entradatexto/login.html', {'form': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'entradatexto/login.html', {'form': form})

def searchView(request):
    query = request.GET.get('search')
    if query:
        usuarios = User.objects.filter(username__icontains=query)
        if not usuarios.exists():
            messages.error(request, 'Usuario no encontrado.')
    else:
        usuarios = User.objects.all()
    
    return render(request, 'entradatexto/search.html', {'users': usuarios})
def LogoutView(request):
    logout(request)
    return redirect('index')

@login_required
def user_profile(request, user):
    username = get_object_or_404(User, pk=user)
    return render(request, 'entradatexto/user_profile.html', {'username': username})

@login_required
def home(request):
    return render(request, 'entradatexto/home.html')

@login_required
def crearcomentario(request):
    if request.method == 'GET':
        return render(request, 'entradatexto/crearcomentario.html', {'formulario': formularioforms()})
    else:
        form = formularioforms(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Comentario creado correctamente.')
            return redirect('listacomentarios')
        else:
            messages.error(request, 'Por favor, rellena todos los campos correctamente')
            return render(request, 'entradatexto/crearcomentario.html', {'formulario': form})

@login_required
def listacomentarios(request):
    formularios = formulario.objects.filter(user=request.user)
    return render(request, 'entradatexto/comentarios_listado.html', {'formularios': formularios})

@login_required
def commentupdate(request, id):
    comment = get_object_or_404(formulario, pk=id)
    if request.method == 'GET':
        form = formularioforms(instance=comment)
        return render(request, 'entradatexto/update.html', {'form': form})
    else:
        form = formularioforms(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentario actualizado correctamente.')
            return redirect('listacomentarios')
        else:
            messages.error(request, 'Por favor, rellena todos los campos correctamente.')
            return render(request, 'entradatexto/update.html', {'form': form})

@login_required
def deletecomment(request, id):
    comment = get_object_or_404(formulario, pk=id)
    if request.method == 'POST':
        if 'borrar' in request.POST:
            if request.POST.get('borrar') == 'Si, eliminar':
                comment.delete()
                messages.success(request, 'Comentario eliminado correctamente.')
                return redirect('listacomentarios')
            else:
                messages.info(request, 'Eliminación cancelada.')
                return redirect('listacomentarios')
        else:
            messages.error(request, 'Opción no válida.')
            return redirect('listacomentarios')
    else:
        return render(request, 'entradatexto/comentarioslista.html', {'comment': comment})

@login_required
def configuraciones(request):
    if request.method == 'GET':
        return render(request, 'entradatexto/configuraciones.html')
    else:
        return redirect('login')
