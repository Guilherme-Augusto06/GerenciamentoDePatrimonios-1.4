from django.urls import path
from . import views
urlpatterns = [
        path('', views.homepage, name="homepage"),         # Inclui as urls do app blog
        path('homepageDark', views.homepageDark, name="homepageDark"),   # Inclui as urls do app blog
        path('login', views.login, name="login"),           # Inclui as urls do app blog
        path('cadastro', views.cadastro, name="cadastro"),   # Inclui as urls do app blog
        path('profile', views.profile, name="profile"),       # Inclui as urls do app blog
        path('faq', views.faq, name="faq"),                 # Inclui as urls do app blog
        path('welcomeHomepage', views.welcomeHomepage, name="welcomeHomepage"),   # Inclui as urls do app blog
        path('itens', views.itens, name="itens"),           # Inclui as urls do app blog
]