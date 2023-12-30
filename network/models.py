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
    
# Modelo para las publicaciones.
class Post(models.Model):
    
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)