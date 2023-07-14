# models.py
from django.db import models

class AreaInteresse(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=200)
    func = models.CharField(max_length=100, null=True)
    salario = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    logradouro = models.CharField(max_length=50, null=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50, null=True)
    area_interesse = models.ForeignKey(AreaInteresse, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
