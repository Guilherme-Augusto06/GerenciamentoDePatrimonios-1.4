from django import forms


class FormLogin(forms.Form):
    user = forms.CharField(label="Usuario", max_length=40)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormCadastro(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50)
    nif = forms.CharField(label="NIF", max_length=8)
    sala = forms.CharField(label="Sala", max_length=20)
    email = forms.EmailField(label="Email", max_length=80)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)