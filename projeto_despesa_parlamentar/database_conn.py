# python -m venv dbvenv
# .\dbvenv\Scripts\activate
# pip install psycopg2

import psycopg2

# Configurações de conexão
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'camara_db',  # Mude para o nome do seu banco de dados
    'user': 'postgres',  # Mude para o seu usuário
    'password': 'admin'  # Mude para a sua senha
}

def conectar():
    """Conecta ao banco de dados PostgreSQL e retorna a conexão."""
    print("Tentando conectar com o banco de dados.")
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        # O autocommit deve ser False por padrão para transações
        print("Conexão com o banco de dados estabelecida com sucesso.")
        return conn
    except psycopg2.DatabaseError as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None

conectar()
