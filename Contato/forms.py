from django import forms
from Contato.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].queryset = Contato.objects.all()
