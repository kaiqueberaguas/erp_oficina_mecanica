from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    contato = models.CharField(max_length=20, verbose_name="Contato (Telefone/Email)")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
    
class Carro(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='carros')
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=8, unique=True, verbose_name="Placa")

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa}) - {self.cliente.nome}"