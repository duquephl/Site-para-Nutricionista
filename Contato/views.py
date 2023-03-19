from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from Contato.forms import ContatoForm
from Contato.models import Contato


# Create your views here.

class CreateContatoView(CreateView):
    model = Contato
    form_class = ContatoForm
    success_url = '/'
