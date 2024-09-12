from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from AppGDP.models import Senai
from AppGDP.forms import FormLogin

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
            var_usuario = form.cleaned_data['user']
            var_senha = form.cleaned_data['password']
            
            user = authenticate(username=var_usuario, password=var_senha)

            if user is not None:
                auth_login(request, user)
                if user.groups.filter(name='Coordenador').exists():
                    return redirect('/homepageAdmin')
                elif user.groups.filter(name='Professor').exists():
                    return redirect('/homepageProfessor')
                else:
                    return redirect('/')
            else:
                print('Login falhou')
    else:
        form = FormLogin()
        context['form'] = form
    return render(request, 'login.html', context)