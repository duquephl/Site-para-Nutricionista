from django.contrib import admin
from django.urls import path, include

from Contato.views import ContatoView

urlpatterns = [
    path('', ContatoView.as_view(), name='contato'),
]
