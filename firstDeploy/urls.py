from django.urls import path
from . import views

urlpatterns = [
     path('', views.deploy, name = "deploy"),
    # path('welcome', views.welcome, name="my welcome"),
    # path('user', views.user, name = "myuser"),
]