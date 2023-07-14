from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Funcionario
from .forms import FuncionarioForm

def agro(request):
    return render(request, 'agro.html')

def registro(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'index.html', {'funcionarios': funcionarios})

def salvar(request):
    if request.method == 'POST':
        nome = request.POST.get("nome")
        data_nascimento = request.POST.get("data_nascimento")
        cpf = request.POST.get("cpf")
        endereco = request.POST.get("endereco")
        func = request.POST.get("func")
        salario = request.POST.get("salario")
        logradouro = request.POST.get("logradouro")
        complemento = request.POST.get("complemento")
        password = request.POST.get("password")

        funcionario = Funcionario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco, func=func, salario=salario, logradouro=logradouro, complemento=complemento, password=password)
        funcionario.save()

    return redirect('agro')

def editar(request, id):
    funcionario = Funcionario.objects.get(id=id)
    return render(request, 'update.html', {'funcionario': funcionario})

def update(request, id):
    if request.method == 'POST':
        funcionario = Funcionario.objects.get(id=id)
        funcionario.nome = request.POST.get('nome')
        funcionario.data_nascimento = request.POST.get('data_nascimento')
        funcionario.cpf = request.POST.get('cpf')
        funcionario.endereco = request.POST.get('endereco')
        funcionario.func = request.POST.get("func")
        funcionario.salario = request.POST.get("salario")
        funcionario.logradouro = request.POST.get("logradouro")
        funcionario.complemento = request.POST.get("complemento")
        funcionario.save()

    return redirect('adm')

def delete(request, id):
    funcionario = Funcionario.objects.get(id=id)
    funcionario.delete()

    return redirect('adm')

def adm(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'adm.html', {'funcionarios': funcionarios})

def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpfusuario')
        password = request.POST.get('passwordlogin')
        try:
            funcionario = Funcionario.objects.get(cpf=cpf)
            if funcionario.password == password:
                return redirect('agro')
            else:
                messages.error(request, 'Senha incorreta.')
        except Funcionario.DoesNotExist:
            messages.error(request, 'Credenciais inválidas.')

    return render(request, 'login.html')

def setor(request):
    return render(request, 'setor.html')

def adm2(request):
    return render(request, 'adm2.html')



def adm3(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adm3')
    else:
        form = FuncionarioForm()
    
    return render(request, 'adm3.html', {'form': form})


def adm4(request):
    return render(request, 'adm4.html')

def adm5(request):
    return render(request, 'adm5.html')

def adm6(request):
    return render(request, 'adm6.html')

def registre(request):
    return render(request, 'registre.html')



