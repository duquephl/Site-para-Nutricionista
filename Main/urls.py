from django.contrib import admin
from django.urls import path, include
from .views import enviar_mensagem

from Main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('enviar-mensagem/', enviar_mensagem, name='enviar_mensagem'),
]
