from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import FormLogin
from .models import Senai
from .models import Usuario
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def homepageDark(request):
    return render(request, 'homepageDark.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def profile(request):
    return render(request, 'profile.html')

def faq(request):
    return render(request, 'faq.html')

def welcomeHomepage(request):
    return render(request, 'welcomeHomepage.html')

def itens(request):
    return render(request, 'itens.html')

def login(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['password']
            
            # Autenticar o usuário
            try:
                usuario = Usuario.objects.get(email=email, senha=senha)
                # Se o usuário existir, faça o login manualmente
                auth_login(request, usuario)
                return redirect('/profile')  # Redireciona após login bem-sucedido
            except Usuario.DoesNotExist:
                messages.error(request, 'Login falhou. Verifique suas credenciais.')
    else:
        form = FormLogin()
    
    context['form'] = form
    return render(request, 'login.html', context)