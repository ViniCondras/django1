from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2,max_digits=8)
    estoque = models.IntegerField ('Quantidade em Estoque')
    custo = models.DecimalField('Preço Custo', decimal_places=2,max_digits=8, default=0)

    def __str__(self):
        return self.nome

class Cliente (models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=7)
    tipo = models.CharField('TipoVeiculo', max_length=15)
    cor = models.CharField('Cor', max_length=20)
    marca = models.CharField('Marca', max_length=20, default='sem marca')

    def __str__(self):
        return f'{self.placa} {self.tipo} {self.cor}'




