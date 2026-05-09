from django.contrib import admin
from .models import Cliente, Carro, OrdemServico

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'contato')
    search_fields = ('nome', 'cpf')

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa', 'modelo', 'cliente')
    search_fields = ('placa', 'cliente__nome')

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'carro', 'get_cliente', 'status', 'valor_servico', 'data_entrada_carro')
    search_fields = ('carro__placa', 'carro__cliente__nome')
    list_filter = ('status',)

    @admin.display(description='Cliente')
    def get_cliente(self, obj):
        return obj.carro.cliente
