from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo personalizado de usuario.
class CustomUser(AbstractUser):
    
    # Campos requeridos.
    correo = models.EmailField(unique=True)
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    
    # Campos adicionales.
    biografia = models.TextField(blank=True)

    def __str__(self):
        return self.username

# Modelo para el manejo de los seguidores.
class Seguidor(models.Model):
    
    seguidor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="seguidor")
    siguiendo = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="siguiendo")
    
    def __str__(self):
        return f"{self.seguidor.username} sigue a {self.siguiendo.username}"
    
# Modelo para el manejo de los likes.
class Like(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} dio like a {self.post}"
    
# Modelo para las publicaciones.
class Post(models.Model):
    
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, through=Like, related_name='post_likes')
    
    def __str__(self):
        return f"Post de {self.autor.username} - {self.contenido}"