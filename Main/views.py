from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Mensagem
from django.http import HttpResponse


# Create your views here.

class HomeView(TemplateView):
    template_name = 'Main/home.html'


class SobreView(TemplateView):
    template_name = 'Main/sobre.html'
