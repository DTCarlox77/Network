from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login as auth_login
from network.models import CustomUser, Post, Seguidor, Like
from django.db.models import Q
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

# Página de presentación de la aplicación.
def main(request):
    return render(request, 'index.html')

# Página para iniciar sesión.
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

# Página del registro de usuarios.
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

# Página pública de los posts.
def posts(request):
    
    # Obtención de las publicaciones ordenadas por fecha.
    all_posts = Post.objects.all().order_by('-fecha')
    
    # Sistema de paginación de la vista.
    paginator = Paginator(all_posts, 10)
    page = request.GET.get('page')
    
    try:
        page_posts = paginator.page(page)
        
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    
    return render(request, 'posts.html', {'posts': page_posts})

@login_required
def following(request):
    
    # Obtención de los usuarios a los que sigue el usuario actual
    usuarios_seguidos = Seguidor.objects.filter(seguidor=request.user).values_list('siguiendo', flat=True)

    # Obtención de las publicaciones de los usuarios seguidos
    following_posts = Post.objects.filter(autor__in=usuarios_seguidos).order_by('-fecha')
    
    # Sistema de paginación de la vista.
    paginator = Paginator(following_posts, 10)
    page = request.GET.get('page')
    
    try:
        page_posts = paginator.page(page)
        
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
    
    return render(request, 'following.html', {'posts': page_posts})

# Vista para hacer una publicación, acá son visibles todas las publicaciones que uno mismo hizo.
@login_required
def new_post(request):
    
    if request.method == 'POST':
        
        autor = request.user
        contenido = request.POST.get('post_description')
        
        nueva_publicacion = Post(autor=autor, contenido=contenido)
        nueva_publicacion.save()
        
    return render(request, 'new.html')

# Perfil propio o de otros usuarios.
def profile(request, username):
    usuario = get_object_or_404(CustomUser, username=username)
    user_posts = Post.objects.filter(autor=usuario).order_by('-fecha')
    seguidor = None

    # Sistema de paginación de la vista.
    paginator = Paginator(user_posts, 10)
    page = request.GET.get('page')

    try:
        page_posts = paginator.page(page)

    except PageNotAnInteger:
        page_posts = paginator.page(1)

    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)
        
    # Cantidad de seguidores del usuario.
    seguidores = Seguidor.objects.filter(siguiendo=usuario).count()
    siguiendo = Seguidor.objects.filter(seguidor=usuario).count()
    
    # Validación de seguimiento de usuario.
    if request.user.is_authenticated:
        seguidor = Seguidor.objects.filter(seguidor=request.user, siguiendo=usuario).exists()
        
    if request.method == 'POST':
        nueva_biografia = request.POST.get('biografia')

        if nueva_biografia is not None:
            usuario.biografia = nueva_biografia
            usuario.save()
        
    return render(request, 'profile.html', {
        'page_posts': page_posts,
        'perfil': 'propio' if str(username) == str(request.user) else None,
        'username': usuario,
        'seguidores': seguidores,
        'siguiendo': siguiendo,
        'seguidor': seguidor
    })

# Función para el manejo de los likes en las publicaciones.
@login_required
def post_liked(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Validación si el usuario ya dio like al post seleccionado.
    like, created = Like.objects.get_or_create(usuario=request.user, post=post)
    
    if created:
        # Agrega a la base de datos el like en caso de ser nuevo like.
        post.likes.add(request.user)
    
    else:
        # Quita el like dela base de datos.
        post.likes.remove(request.user)
    
    # Cantidad de likes del post.
    cantidad_likes = post.likes.count()
    
    return JsonResponse({
        'likes': cantidad_likes
    })
    
@login_required
def del_post(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)
    
    if request.user == post.autor:
        Post.objects.filter(id=post_id, autor=request.user).delete()
        return HttpResponse("success")
        
    return redirect('profile')

@login_required
def edit_post(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)
    data = json.loads(request.body)
    
    nuevo_post = data.get('nuevo_post', '')
    
    if request.user == post.autor:
        post.contenido = nuevo_post
        post.save()
        
        return JsonResponse({
            'post_actualizado': post.contenido
        })
        
    return redirect('profile')

# Función para el manejo de los seguidores.
@login_required
def follow_user(request, username):
    usuario_seguido = get_object_or_404(CustomUser, username=username)
    
    # Condición para dejar de seguir.
    if Seguidor.objects.filter(seguidor=request.user, siguiendo=usuario_seguido).exists():
        Seguidor.objects.filter(seguidor=request.user, siguiendo=usuario_seguido).delete()
    
    # Condición para seguir a un usuario.
    else:
        Seguidor.objects.create(seguidor=request.user, siguiendo=usuario_seguido)
        
    cantidad_seguidores = Seguidor.objects.filter(siguiendo=usuario_seguido).count()
    
    return JsonResponse({
        'seguidores': cantidad_seguidores
    })

# Cierre de sesión de la aplicación.
@login_required
def exit(request):
    logout(request)
    return redirect('login')