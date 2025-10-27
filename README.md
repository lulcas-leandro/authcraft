# AuthCraft

Sistema de autenticação completo desenvolvido com Flask.

## Sobre o Projeto

AuthCraft é uma aplicação web que implementa um sistema de autenticação de usuários, incluindo registro, login e gerenciamento de sessões. O projeto foi desenvolvido seguindo padrões modernos de arquitetura Flask e design patterns.

## Tecnologias Utilizadas

- **Python 3.8+** - Linguagem de programação
- **Flask** - Framework web minimalista
- **SQLAlchemy** - ORM para gerenciamento de banco de dados
- **Flask-Login** - Gerenciamento de sessões de usuário
- **Flask-Migrate** - Controle de versão do banco de dados
- **Flask-WTF** - Formulários com validação
- **Werkzeug** - Criptografia de senhas
- **Bootstrap 5** - Framework CSS para interface responsiva

## Funcionalidades

- Registro de novos usuários com validação de dados
- Sistema de login seguro com senhas criptografadas
- Gerenciamento de sessões com Flask-Login
- Dashboard personalizado para usuários autenticados
- Proteção de rotas privadas
- Validações de formulário no cliente e servidor
- Interface responsiva e moderna
- Mensagens de feedback para o usuário

## Estrutura do Projeto

```
AuthCraft/
├── app/
│   ├── auth/              # Blueprint de autenticação
│   │   ├── __init__.py
│   │   ├── forms.py       # Formulários de login e registro
│   │   └── routes.py      # Rotas de autenticação
│   ├── main/              # Blueprint principal
│   │   ├── __init__.py
│   │   └── routes.py      # Rotas públicas e dashboard
│   ├── models/            # Modelos do banco de dados
│   │   └── user.py        # Modelo de usuário
│   ├── templates/         # Templates HTML
│   │   ├── auth/
│   │   ├── main/
│   │   └── base.html
│   ├── static/            # Arquivos estáticos
│   ├── __init__.py        # Application Factory
│   └── config.py          # Configurações da aplicação
├── migrations/            # Migrações do banco de dados
├── .env                   # Variáveis de ambiente
├── .gitignore
├── requirements.txt       # Dependências do projeto
└── run.py                 # Ponto de entrada da aplicação
```

## Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a passo

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/AuthCraft.git
cd AuthCraft
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

Crie um arquivo `.env` na raiz do projeto:
```
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///authcraft.db
```

5. Inicialize o banco de dados:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Execute a aplicação:
```bash
python run.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`

## Uso

1. Acesse a página inicial
2. Clique em "Registrar" para criar uma nova conta
3. Preencha o formulário com seus dados
4. Faça login com suas credenciais
5. Acesse o dashboard personalizado

## Padrões e Boas Práticas

- **Application Factory Pattern**: Permite múltiplas instâncias da aplicação
- **Blueprints**: Organização modular do código
- **Migrations**: Controle de versão do banco de dados
- **Validações**: Proteção contra dados inválidos
- **Segurança**: Senhas criptografadas com hash
- **Separação de responsabilidades**: Models, Views e Controllers bem definidos

