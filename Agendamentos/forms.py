from django import forms
from Agendamentos.models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'data', 'horario']

    def save(self, commit=True):
        agendamento = super(AgendamentoForm, self).save(commit=False)
        agendamento.status = 'A'
        agendamento.Data_Hora = str(agendamento.data) + ' ' + agendamento.horario
        if Agendamento.objects.filter(Data_Hora=agendamento.Data_Hora).exists():
            raise forms.ValidationError('Horário indisponível')
        elif commit:
            agendamento.save()
        return agendamento