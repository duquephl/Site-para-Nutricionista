from django.shortcuts import render
from django.views import View


# Create your views here.

class ContatoView(View):
    template_name = 'contato.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        contato = Contato(nome=nome, email=email, mensagem=mensagem)
        contato.save()
        return render(request, self.template_name, {'success_message': 'Mensagem enviada com sucesso!'})