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
