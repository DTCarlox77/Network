from .views import *
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('login/', login, name='login'),
    path('sign_in/', sign_in, name='sign_in'),
    path('posts/', posts, name='posts'),
    path('new_post/', new_post, name='new'),
    path('profile/', profile, name='profile'),
    path('logout/', exit, name='exit'),
    path('following/', main, name='following')
]