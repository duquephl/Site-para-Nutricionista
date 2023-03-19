from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Mensagem
from django.http import HttpResponse

def enviar_mensagem(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        assunto = request.POST['assunto']
        mensagem = request.POST['mensagem']
        
        nova_mensagem = Mensagem(nome=nome, email=email, mensagem=mensagem)
        nova_mensagem.save()
        
        return HttpResponse('Mensagem enviada com sucesso!')
    
    return render(request, 'seu_template.html')

# Create your views here.

class HomeView(TemplateView):
    template_name = 'Main/home.html'

