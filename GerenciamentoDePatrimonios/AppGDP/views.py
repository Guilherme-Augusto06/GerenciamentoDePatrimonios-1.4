from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import FormLogin, formCadastroUsuario, InventarioForm
from .models import Senai
from django.contrib.auth.models import User
from .models import Inventario


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')

def homepageDark(request):
    return render(request, 'homepageDark.html')

def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')

def faq(request):
    return render(request, 'faq.html')

def welcomeHomepage(request):
    return render(request, 'welcomeHomepage.html')

# Importar o modelo de itens (substitua Item pelo nome correto do seu modelo)


def itens(request):
    inventario = Inventario.objects.all()
    item_especifico = inventario.first()  # ou qualquer outro critério para escolher o item
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itens')  # Redireciona para a página de itens
    else:
        form = InventarioForm()
    
    return render(request, 'itens.html', {'form': form, 'inventario': inventario, 'item_especifico': item_especifico})

def adicionar_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itens')  # Redireciona para a página de itens
    else:
        form = InventarioForm()
    
    return render(request, 'itens.html', {'form': form, 'inventario': Inventario.objects.all()})


def cadastroUsuario(request):
    context = {}
    dadosSenai = Senai.objects.all()
    context["dadosSenai"] = dadosSenai
    if request.method == 'POST':
        form = formCadastroUsuario(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['first_name']
            var_sobrenome = form.cleaned_data['last_name']
            var_usuario = form.cleaned_data['user']
            var_email = form.cleaned_data['email']
            var_senha = form.cleaned_data['password']

            user = User.objects.create_user(username=var_usuario, email=var_email, password=var_senha)
            user.first_name = var_nome
            user.last_name = var_sobrenome
            user.save()
            return redirect('/login')
            print('Cadastro realizado com sucesso')
    else:
        form = formCadastroUsuario()
        context['form'] = form
        print('Cadastro falhou')
    return render(request, 'cadastroUsuario.html', context)

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
                return redirect('/welcomeHomepage')  
            else:
                print('Login falhou')
    else:
        form = FormLogin()
        context['form'] = form
        return render(request, 'login.html', context)
    

def buscar_itens(request):
    query = request.GET.get('q')  # Pega o valor digitado no campo de busca
    if query:
        inventario = Inventario.objects.filter(num_inventario__icontains=query)
    else:
        inventario = Inventario.objects.all()
    
    return render(request, 'seu_template.html', {'inventario': inventario})