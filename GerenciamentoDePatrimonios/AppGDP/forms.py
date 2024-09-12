from django import forms

class FormLogin(forms.Form):
    email = forms.EmailField(label="Email", max_length=80, widget=forms.EmailInput(attrs={
        'class': 'input-login',
        'placeholder': 'Insira seu email'
    }))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={
        'class': 'input-login',
        'placeholder': 'Insira sua senha'
    }))


class FormCadastro(forms.Form):
    nome = forms.CharField(label="Nome", max_length=50)
    nif = forms.CharField(label="NIF", max_length=8)
    sala = forms.CharField(label="Sala", max_length=20)
    email = forms.EmailField(label="Email", max_length=80)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)