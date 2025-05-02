## CoinData

Projeto em Django e Django REST Framework para coleta e visualização do preço do Bitcoin a cada minuto.

## 📄 Visão Geral

O CoinData é uma aplicação backend que coleta o preço do Bitcoin (BTC) via API da CoinGecko a cada 1 minuto, armazena os dados com timestamp em um banco de dados PostgreSQL e disponibiliza os dados via API REST. Os dados serão posteriormente visualizados em tempo real via Grafana.

## 📁 Estrutura do Projeto

```
coindata_project/
├── coindata/            # Configurações do projeto Django
├── prices/              # App responsável pela coleta e API de preços
├── logs/                # Logs gerados pelo cron
├── .env                 # Variáveis de ambiente
├── run_fetch.sh         # Script usado pelo cron para coleta
├── manage.py
└── requirements.txt
```

## ⚙️ Tecnologias

* Python 3.12
* Django 5.x
* Django REST Framework
* PostgreSQL
* requests
* python-decouple
* Cron (para agendamento da coleta)

## 🔄 Setup do Ambiente

```bash
# Clonar o repositório
$ git clone https://github.com/seu-usuario/coindata.git
$ cd coindata

# Criar ambiente virtual
$ python3 -m venv env
$ source env/bin/activate

# Instalar dependências
$ pip install -r requirements.txt

# Criar .env com as configurações:
$ cp .env.example .env

# Realizar migrações
$ python manage.py migrate

# Iniciar o servidor
$ python manage.py runserver
```

## 📊 Banco de Dados

Certifique-se de criar o banco PostgreSQL antes de rodar as migrações:

```sql
CREATE DATABASE coindata;
CREATE USER coindatauser WITH PASSWORD 'senha';
GRANT ALL PRIVILEGES ON DATABASE coindata TO coindatauser;
```

## ⏰ Coleta Automática com Cron

O script `run_fetch.sh` executa a coleta do preço do Bitcoin e deve ser agendado no `crontab`:

```bash
* * * * * /caminho/para/coindata/run_fetch.sh >> /caminho/para/coindata/logs/cron.log 2>&1
```

## 📆 API Endpoints

* `GET /api/prices/` - Lista de preços do Bitcoin
* `GET /api/prices/<id>/` - Detalhes de um preço específico

## 🌐 Futuro

* Integração com Grafana
* Filtros por data e preço
* Exportação CSV
* Autenticação JWT

Autor: 
Tiago Monteiro



