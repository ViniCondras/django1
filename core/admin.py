from django.contrib import admin

from .models import Produto, Cliente, Veiculo
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','preco','estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email')

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id','placa','tipo','cor')


admin.site.register (Produto, ProdutoAdmin)
admin.site.register (Cliente, ClienteAdmin)
admin.site.register (Veiculo, VeiculoAdmin)
