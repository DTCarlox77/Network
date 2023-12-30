from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.login, name="login"),
    path('sign_in', views.sign_in, name="sign_in")
]