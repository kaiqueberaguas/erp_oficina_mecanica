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

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='ordens')
    descricao_ordem = models.TextField(verbose_name="Descrição da Ordem")
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do Serviço")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    data_entrada_carro = models.DateField(verbose_name="Data de Entrada do Carro")
    data_inicio_servico = models.DateField(null=True, blank=True, verbose_name="Data de Início do Serviço")
    data_fim_servico = models.DateField(null=True, blank=True, verbose_name="Data de Fim do Serviço")
    data_retirada_veiculo = models.DateField(null=True, blank=True, verbose_name="Data de Retirada do Veículo")

    class Meta:
        verbose_name = "Ordem de Serviço"
        verbose_name_plural = "Ordens de Serviço"

    def __str__(self):
        return f"OS #{self.pk} - {self.carro} ({self.status})"