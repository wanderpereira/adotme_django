from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect

# Create your views here.  

def cadastro(request):
    #Verifica se está autenticado
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
    if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
        return render(request, 'cadastro.html')
    try:
            user = User.objects.create_user(
                username=email,
                email=nome,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário foi criado com Sucesso!')
            return render(request, 'cadastro.html')
    except:
            messages.add_message(request, constants.SUCCESS, 'Erro interno: 1025 - Exception module auth!')
            return render(request, 'cadastro.html')

def logar(request):
    #Verifica se está autenticado
    if request.user.is_authenticated:
        return redirect('/adotar')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = authenticate(username=email, password=senha)
        
        if user is not None:
           login(request, user)
           return redirect('/adotar')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos!')
            return render(request, 'login.html')
            
def sair(request):
    logout(request)
    return redirect('/auth/login')