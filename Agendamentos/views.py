from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from django.urls import reverse_lazy

from Agendamentos.models import Agendamento

class CreateAgendamentoView(CreateView):
    model = Agendamento
    template_name = 'agendamento.html'
    fields = ['nome', 'data', 'horario']
    success_url = reverse_lazy('agendamento')

