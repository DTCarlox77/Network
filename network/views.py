from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login
from network.models import CustomUser
from django.db import IntegrityError

# Create your views here.
def main(request):
    return render(request, 'index.html')

@csrf_protect
def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            
            # Verifica si existe una ruta de redirección (next).
            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url:
                return redirect(next_url)
            
            # Si no hay una ruta de redirección, redirigir a 'posts'.
            return redirect('posts')
        else:
            return render(request, 'registration/login.html', {'mensaje': 'Credenciales incorrectas. Por favor, inténtalo de nuevo.'})
    
    return render(request, 'registration/login.html')

@csrf_protect
def sign_in(request):
    
    if request.method == 'POST':
        # Validación de los datos del formulario.
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        
        respaldo = {
            'username': username,
            'password': password,
            'name': name,   
            'lastname': lastname,
            'email': email
        }
        
        if not username or not password or not name or not lastname or not email:
            return render(request, 'registration/sign_in.html', {
                'mensaje': 'Completa todos los campos para registrarte',
                'respaldo': respaldo
            })
        
        if not username.isalnum():
            return render(request, 'registration/sign_in.html', {
                'mensaje': 'El nombre de usuario no puede contener caracteres especiales',
                'respaldo': respaldo
            })
        
        if len(password) < 5:
            return render(request, 'registration/sign_in.html', {
                'mensaje': 'La contraseña ingresada es muy corta',
                'respaldo': respaldo
            })
            
        try:
            user = CustomUser.objects.create_user(username=username, password=password, name=name, lastname=lastname, correo=email)
            return redirect('login')
        
        except IntegrityError as e:
            if 'UNIQUE constraint' in str(e):
                return render(request, 'registration/sign_in.html', {
                    'mensaje': 'El correo o nombre de usuario ya están en uso. Por favor, elige otro.',
                    'respaldo': respaldo
                })
            else:
                return render(request, 'registration/sign_in.html', {
                    'mensaje': f'Error de registro: {e}',
                    'respaldo': respaldo
                })
        
    return render(request, 'registration/sign_in.html')

@login_required
def posts(request):
    return render(request, 'posts.html')

@login_required
def new_post(request):
    return render(request, 'new.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def exit(request):
    logout(request)
    return redirect('login')