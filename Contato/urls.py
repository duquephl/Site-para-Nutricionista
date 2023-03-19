from django.contrib import admin
from django.urls import path, include

from Contato.views import CreateContatoView

urlpatterns = [
    path('', CreateContatoView.as_view(), name='contato'),
]
