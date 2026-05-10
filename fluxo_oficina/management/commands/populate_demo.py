from datetime import date
from django.core.management.base import BaseCommand
from fluxo_oficina.models import Cliente, Carro, OrdemServico

CLIENTES = [
    {"nome": "Carlos Eduardo Mendes", "cpf": "123.456.789-00", "contato": "(11) 98765-4321"},
    {"nome": "Ana Paula Ferreira", "cpf": "234.567.890-11", "contato": "anapaula@gmail.com"},
    {"nome": "Roberto Souza Lima", "cpf": "345.678.901-22", "contato": "(21) 91234-5678"},
    {"nome": "Mariana Costa Alves", "cpf": "456.789.012-33", "contato": "(31) 99876-5432"},
    {"nome": "João Pedro Oliveira", "cpf": "567.890.123-44", "contato": "joaopedro@hotmail.com"},
    {"nome": "Fernanda Ramos Silva", "cpf": "678.901.234-55", "contato": "(41) 98888-1234"},
    {"nome": "Lucas Barbosa Teixeira", "cpf": "789.012.345-66", "contato": "(51) 97777-9999"},
    {"nome": "Patrícia Gomes Martins", "cpf": "890.123.456-77", "contato": "patricia.gomes@email.com"},
    {"nome": "Thiago Nascimento Cruz", "cpf": "901.234.567-88", "contato": "(61) 96666-7777"},
    {"nome": "Juliana Cardoso Pinto", "cpf": "012.345.678-99", "contato": "(71) 95555-3333"},
]

CARROS = [
    {"cliente_cpf": "123.456.789-00", "marca": "Fiat", "modelo": "Uno", "placa": "ABC1D23"},
    {"cliente_cpf": "123.456.789-00", "marca": "Volkswagen", "modelo": "Gol", "placa": "XYZ2E45"},
    {"cliente_cpf": "234.567.890-11", "marca": "Chevrolet", "modelo": "Onix", "placa": "DEF3F67"},
    {"cliente_cpf": "345.678.901-22", "marca": "Ford", "modelo": "Ka", "placa": "GHI4G89"},
    {"cliente_cpf": "345.678.901-22", "marca": "Toyota", "modelo": "Corolla", "placa": "JKL5H01"},
    {"cliente_cpf": "456.789.012-33", "marca": "Fiat", "modelo": "Palio", "placa": "MNO6I23"},
    {"cliente_cpf": "567.890.123-44", "marca": "Volkswagen", "modelo": "Polo", "placa": "PQR7J45"},
    {"cliente_cpf": "567.890.123-44", "marca": "Hyundai", "modelo": "HB20", "placa": "STU8K67"},
    {"cliente_cpf": "678.901.234-55", "marca": "Chevrolet", "modelo": "Tracker", "placa": "VWX9L89"},
    {"cliente_cpf": "789.012.345-66", "marca": "Ford", "modelo": "EcoSport", "placa": "YZA0M01"},
    {"cliente_cpf": "890.123.456-77", "marca": "Renault", "modelo": "Sandero", "placa": "BCD1N23"},
    {"cliente_cpf": "890.123.456-77", "marca": "Fiat", "modelo": "Strada", "placa": "EFG2O45"},
    {"cliente_cpf": "901.234.567-88", "marca": "Toyota", "modelo": "Hilux", "placa": "HIJ3P67"},
    {"cliente_cpf": "012.345.678-99", "marca": "Volkswagen", "modelo": "Saveiro", "placa": "KLM4Q89"},
    {"cliente_cpf": "012.345.678-99", "marca": "Chevrolet", "modelo": "S10", "placa": "NOP5R01"},
]

ORDENS = [
    # Finalizadas
    {"placa": "ABC1D23", "descricao": "Troca de óleo e filtro", "valor": "250.00", "status": "finalizada",
     "data_entrada": date(2026, 1, 5), "data_inicio": date(2026, 1, 5), "data_fim": date(2026, 1, 5), "data_retirada": date(2026, 1, 6)},
    {"placa": "XYZ2E45", "descricao": "Revisão completa: freios, suspensão e alinhamento", "valor": "980.00", "status": "finalizada",
     "data_entrada": date(2026, 1, 10), "data_inicio": date(2026, 1, 11), "data_fim": date(2026, 1, 14), "data_retirada": date(2026, 1, 15)},
    {"placa": "DEF3F67", "descricao": "Substituição de correia dentada", "valor": "650.00", "status": "finalizada",
     "data_entrada": date(2026, 1, 20), "data_inicio": date(2026, 1, 20), "data_fim": date(2026, 1, 21), "data_retirada": date(2026, 1, 22)},
    {"placa": "GHI4G89", "descricao": "Troca de pastilhas de freio dianteiras e traseiras", "valor": "420.00", "status": "finalizada",
     "data_entrada": date(2026, 2, 3), "data_inicio": date(2026, 2, 3), "data_fim": date(2026, 2, 3), "data_retirada": date(2026, 2, 4)},
    {"placa": "JKL5H01", "descricao": "Troca de amortecedores dianteiros", "valor": "1200.00", "status": "finalizada",
     "data_entrada": date(2026, 2, 8), "data_inicio": date(2026, 2, 9), "data_fim": date(2026, 2, 10), "data_retirada": date(2026, 2, 11)},
    {"placa": "MNO6I23", "descricao": "Diagnóstico eletrônico e limpeza de bicos injetores", "valor": "380.00", "status": "finalizada",
     "data_entrada": date(2026, 2, 15), "data_inicio": date(2026, 2, 15), "data_fim": date(2026, 2, 16), "data_retirada": date(2026, 2, 17)},
    {"placa": "PQR7J45", "descricao": "Troca de bateria e revisão elétrica", "valor": "550.00", "status": "finalizada",
     "data_entrada": date(2026, 3, 1), "data_inicio": date(2026, 3, 1), "data_fim": date(2026, 3, 1), "data_retirada": date(2026, 3, 2)},
    {"placa": "STU8K67", "descricao": "Alinhamento, balanceamento e rodízio de pneus", "valor": "180.00", "status": "finalizada",
     "data_entrada": date(2026, 3, 10), "data_inicio": date(2026, 3, 10), "data_fim": date(2026, 3, 10), "data_retirada": date(2026, 3, 10)},
    {"placa": "VWX9L89", "descricao": "Troca de embreagem completa", "valor": "1800.00", "status": "finalizada",
     "data_entrada": date(2026, 3, 18), "data_inicio": date(2026, 3, 19), "data_fim": date(2026, 3, 22), "data_retirada": date(2026, 3, 23)},
    {"placa": "YZA0M01", "descricao": "Reparo no sistema de ar-condicionado (carga de gás e troca de filtro)", "valor": "490.00", "status": "finalizada",
     "data_entrada": date(2026, 4, 2), "data_inicio": date(2026, 4, 2), "data_fim": date(2026, 4, 3), "data_retirada": date(2026, 4, 4)},
    {"placa": "BCD1N23", "descricao": "Troca de velas e cabos de ignição", "valor": "310.00", "status": "finalizada",
     "data_entrada": date(2026, 4, 14), "data_inicio": date(2026, 4, 14), "data_fim": date(2026, 4, 14), "data_retirada": date(2026, 4, 15)},
    {"placa": "EFG2O45", "descricao": "Revisão de 30.000 km: óleo, filtros e freios", "valor": "750.00", "status": "finalizada",
     "data_entrada": date(2026, 4, 22), "data_inicio": date(2026, 4, 22), "data_fim": date(2026, 4, 24), "data_retirada": date(2026, 4, 25)},
    # Abertas (em andamento)
    {"placa": "HIJ3P67", "descricao": "Troca de diferencial traseiro — aguardando peça importada", "valor": "3200.00", "status": "aberta",
     "data_entrada": date(2026, 4, 28), "data_inicio": date(2026, 4, 29), "data_fim": None, "data_retirada": None},
    {"placa": "KLM4Q89", "descricao": "Reparo na caixa de câmbio manual", "valor": "2100.00", "status": "aberta",
     "data_entrada": date(2026, 5, 2), "data_inicio": date(2026, 5, 3), "data_fim": None, "data_retirada": None},
    {"placa": "NOP5R01", "descricao": "Substituição de junta de cabeçote", "valor": "1650.00", "status": "aberta",
     "data_entrada": date(2026, 5, 5), "data_inicio": date(2026, 5, 6), "data_fim": None, "data_retirada": None},
    {"placa": "ABC1D23", "descricao": "Troca de pneus (4 unidades) e alinhamento", "valor": "1400.00", "status": "aberta",
     "data_entrada": date(2026, 5, 7), "data_inicio": None, "data_fim": None, "data_retirada": None},
    {"placa": "DEF3F67", "descricao": "Verificação de barulho na suspensão traseira", "valor": "120.00", "status": "aberta",
     "data_entrada": date(2026, 5, 8), "data_inicio": None, "data_fim": None, "data_retirada": None},
    {"placa": "GHI4G89", "descricao": "Troca de radiador e mangueiras do sistema de arrefecimento", "valor": "890.00", "status": "aberta",
     "data_entrada": date(2026, 5, 9), "data_inicio": date(2026, 5, 10), "data_fim": None, "data_retirada": None},
    {"placa": "MNO6I23", "descricao": "Revisão completa pré-viagem longa", "valor": "600.00", "status": "aberta",
     "data_entrada": date(2026, 5, 10), "data_inicio": None, "data_fim": None, "data_retirada": None},
    # Canceladas
    {"placa": "PQR7J45", "descricao": "Reparo na lataria após colisão leve — cliente desistiu", "valor": "2500.00", "status": "cancelada",
     "data_entrada": date(2026, 2, 20), "data_inicio": None, "data_fim": None, "data_retirada": None},
    {"placa": "STU8K67", "descricao": "Troca de motor — orçamento recusado pelo cliente", "valor": "8500.00", "status": "cancelada",
     "data_entrada": date(2026, 3, 5), "data_inicio": None, "data_fim": None, "data_retirada": None},
    {"placa": "VWX9L89", "descricao": "Instalação de kit GNV — cliente transferiu para outra oficina", "valor": "3200.00", "status": "cancelada",
     "data_entrada": date(2026, 4, 10), "data_inicio": date(2026, 4, 10), "data_fim": None, "data_retirada": None},
    {"placa": "YZA0M01", "descricao": "Pintura completa do veículo — fora do escopo, encaminhado para funilaria", "valor": "4000.00", "status": "cancelada",
     "data_entrada": date(2026, 4, 18), "data_inicio": None, "data_fim": None, "data_retirada": None},
    {"placa": "BCD1N23", "descricao": "Diagnóstico de falha intermitente — cancelado por falta de peça nacional", "valor": "150.00", "status": "cancelada",
     "data_entrada": date(2026, 5, 1), "data_inicio": date(2026, 5, 1), "data_fim": None, "data_retirada": None},
]


class Command(BaseCommand):
    help = "Popula o banco de dados com massa de dados para demonstração"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Remove todos os dados existentes antes de inserir",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            OrdemServico.objects.all().delete()
            Carro.objects.all().delete()
            Cliente.objects.all().delete()
            self.stdout.write(self.style.WARNING("Dados anteriores removidos."))

        clientes_criados = 0
        for dados in CLIENTES:
            _, criado = Cliente.objects.get_or_create(cpf=dados["cpf"], defaults={"nome": dados["nome"], "contato": dados["contato"]})
            if criado:
                clientes_criados += 1

        carros_criados = 0
        for dados in CARROS:
            try:
                cliente = Cliente.objects.get(cpf=dados["cliente_cpf"])
            except Cliente.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Cliente {dados['cliente_cpf']} não encontrado."))
                continue
            _, criado = Carro.objects.get_or_create(
                placa=dados["placa"],
                defaults={"cliente": cliente, "marca": dados["marca"], "modelo": dados["modelo"]},
            )
            if criado:
                carros_criados += 1

        ordens_criadas = 0
        for dados in ORDENS:
            try:
                carro = Carro.objects.get(placa=dados["placa"])
            except Carro.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Carro {dados['placa']} não encontrado."))
                continue
            _, criado = OrdemServico.objects.get_or_create(
                carro=carro,
                descricao_ordem=dados["descricao"],
                defaults={
                    "valor_servico": dados["valor"],
                    "status": dados["status"],
                    "data_entrada_carro": dados["data_entrada"],
                    "data_inicio_servico": dados["data_inicio"],
                    "data_fim_servico": dados["data_fim"],
                    "data_retirada_veiculo": dados["data_retirada"],
                },
            )
            if criado:
                ordens_criadas += 1

        self.stdout.write(self.style.SUCCESS(
            f"\nDemo populada com sucesso!\n"
            f"  Clientes criados : {clientes_criados}\n"
            f"  Carros criados   : {carros_criados}\n"
            f"  OS criadas       : {ordens_criadas}"
        ))
