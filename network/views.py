from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def main(request):
    return render(request, 'index.html')

@csrf_protect
def login(request):
    
    if request.method == 'POST':
        # Proceso de los datos del formulario.
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    
    return render(request, 'login.html')

def sign_in(request):
    return render(request, 'sign_in.html')