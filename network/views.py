from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    return render(request, 'index.html')

@csrf_protect
def login(request):
    
    if request.method == 'POST':
        # Proceso de los datos del formulario.
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        respaldo = {
            'username': username,
        }
    
    return render(request, 'login.html')

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
        
        print(respaldo)
        
        if not username or not password or not name or not lastname or not email:
            return render(request, 'sign_in.html', {
                'mensaje': 'Completa todos los campos para registrarte',
                'respaldo': respaldo
            })
        
        if not username.isalnum():
            return render(request, 'sign_in.html', {
                'mensaje': 'El nombre de usuario no puede contener carácteres especiales',
                'respaldo': respaldo
            })
        
        if len(password) < 5:
            return render(request, 'sign_in.html', {
                'mensaje': 'La contraseña ingresada es muy corta',
                'respaldo': respaldo
            })
        
    return render(request, 'sign_in.html')

@login_required
def posts(request):
    return render(request, 'posts.html')

@login_required
def new_post(request):
    return render(request, 'new.html')

@login_required
def profile(request):
    return render(request, 'profile.html')