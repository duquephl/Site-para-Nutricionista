from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from django.urls import reverse_lazy

from Agendamentos.forms import AgendamentoForm
from Agendamentos.models import Agendamento

class CreateAgendamentoView(CreateView):
    model = Agendamento
    form_class = AgendamentoForm
    success_url = reverse_lazy('agendamento')

