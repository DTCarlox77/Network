from .views import *
from django.urls import path

urlpatterns = [
    path('', main, name='main'),
    path('login/', login, name='login'),
    path('sign_in/', sign_in, name='sign_in'),
    path('posts/', posts, name='posts'),
    path('new_post/', new_post, name='new'),
    path('profile/<str:username>/', profile, name='profile'),
    path('logout/', exit, name='exit'),
    path('following/', main, name='following'),
    path('like_post/<int:post_id>/', post_liked, name='like_post'),
    path('follow/<str:username>/', follow_user, name='follow_user'),
    path('del_post/<int:post_id>/', del_post, name='del_post')
]