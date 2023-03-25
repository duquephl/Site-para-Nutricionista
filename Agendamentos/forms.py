from django import forms
from Agendamentos.models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome', 'data', 'horario']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].queryset = Agendamento.objects.all()

    def save(self, commit=True):
        agendamento = super(AgendamentoForm, self).save(commit=False)
        agendamento.status = 'Agendado'
        if commit:
            agendamento.save()
        return agendamento