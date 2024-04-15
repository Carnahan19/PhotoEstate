from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError


# renderizar el html para la pagina principal.
def home(request):
    return render(request, 'home.html')

# renderizar el html para la pagina de montaje virtual.
def vstagin(request):
    return render(request, 'virtualstaging.html')

# renderizar el html para la pagina de mejoras.
def enhancements(request):
    return render(request, 'enhancements.html')

# renderizar el html para la pagina de crepusculo.
def twilight(request):
    return render(request, 'twilight.html')

# renderizar el html para la pagina de planos.
def floorplans(request):
    return render(request, 'floorplans.html')

# renderizar el html para la pagina de registro de usuario.
def signup(request):
    # if else para verificar si el metodo es GET o POST
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})

    else:
        # if para verificar si las contraseñas coinciden
        if request.POST['password1'] == request.POST['password2']:
            # try para verificar si el usuario ya existe
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    "error": 'El usuario ya existe'})
        # else para mostrar un mensaje de error si las contraseñas no coinciden
        return render(request, 'signup.html', {'form': UserCreationForm(), "error": 'Contraseñas no coinciden'})


def tasks(request):
    return render(request, 'task.html')

# funcion para cerrar sesion
def signout(request):   
    logout(request)
    return redirect('home')

# renderizar el html para la pagina de inicio de sesion.
def signin(request):
    # if else para verificar si el metodo es GET o POST
    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        # if para verificar si el usuario y contraseña son correctos
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm, 
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)    
            return redirect('home')

            

        
