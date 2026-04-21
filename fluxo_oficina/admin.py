from django.contrib import admin
from .models import Cliente, Carro

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'contato')
    search_fields = ('nome', 'cpf')

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'placa', 'cliente')
    search_fields = ('marca', 'modelo', 'placa')
    list_filter = ('marca', 'modelo', 'cliente')

