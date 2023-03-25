from django.contrib import admin
from django.urls import path, include

from Agendamentos.views import CreateAgendamentoView

urlpatterns = [
    path('', CreateAgendamentoView.as_view(), name='agendamento'),

]
