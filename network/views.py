from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def sign_in(request):
    return render(request, 'sign_in.html')