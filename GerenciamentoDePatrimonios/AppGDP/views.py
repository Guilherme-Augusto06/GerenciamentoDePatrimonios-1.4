from django.shortcuts import render

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