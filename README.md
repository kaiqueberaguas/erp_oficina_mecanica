# Sistema de Gestão de Oficina Mecânica

Sistema de gerenciamento para oficinas mecânicas desenvolvido com Django. Projeto Integrador — 4º semestre de Engenharia da Computação.

---

## Pré-requisitos

- [Python 3.13+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [VS Code](https://code.visualstudio.com/) *(opcional)*

---

## Configuração do Ambiente de Desenvolvimento

### Windows

**Linha de Comando (cmd/PowerShell)**

```bat
# 1. Clone o repositório
git clone <url-do-repositorio>
cd erp_oficina_mecanica #corrigido o nome do arquivo (any maciel)

# 2. Crie o ambiente virtual
python -m venv venv

# 3. Ative o ambiente virtual
.\venv\Scripts\activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Aplique as migrações
python manage.py migrate

# 6. Crie um superusuário (para acessar o painel admin)
python manage.py createsuperuser

# 7. Inicie o servidor
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

### Linux / macOS

**Terminal**

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd erp_oficina_project

# 2. Crie o ambiente virtual
python3 -m venv venv

# 3. Ative o ambiente virtual
source venv/bin/activate

# 4. Instale as dependências
pip install -r requirements.txt

# 5. Aplique as migrações
python manage.py migrate

# 6. Crie um superusuário (para acessar o painel admin)
python manage.py createsuperuser

# 7. Inicie o servidor
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

---

### VS Code

1. Abra a pasta do projeto: **File → Open Folder** → selecione `erp_oficina_project/`

2. Instale as extensões recomendadas:
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Django](https://marketplace.visualstudio.com/items?itemName=batisteo.vscode-django)

3. Selecione o interpretador Python do ambiente virtual:
   - Pressione `Ctrl+Shift+P`
   - Digite **Python: Select Interpreter**
   - Escolha o interpretador dentro da pasta `venv/`

4. Abra o terminal integrado (`Ctrl+` `` ` ``) e siga os mesmos passos da seção **Windows** ou **Linux** acima (a partir do passo 4, pois o venv já estará ativo).

5. Para rodar o servidor diretamente pelo VS Code, crie o arquivo `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django: Runserver",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": true
    }
  ]
}
```

Depois pressione `F5` para iniciar o servidor com o debugger.

---

## Executando os Testes

```bash
# Testes unitários com Pytest
pytest

# Testes com saída detalhada
pytest -v
```

---

## Painel Administrativo

Após criar o superusuário, acesse: http://127.0.0.1:8000/admin

---

## Estrutura do Projeto

```
erp_oficina_project/
├── configuracoes/       # Settings e URLs do Django
├── fluxo_oficina/       # App principal (Clientes, Veículos, OS)
│   └── tests.py         # Testes unitários e de integração
├── templates/           # Páginas HTML
├── testes_e2e/          # Testes Cypress (E2E)
├── .github/workflows/   # Pipelines de CI/CD
├── manage.py
├── requirements.txt
└── README.md
```
