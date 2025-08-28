# python -m venv dbvenv
# .\dbvenv\Scripts\activate
# pip install psycopg2

import psycopg2

# Configurações de conexão
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'database_demo',  # Mude para o nome do seu banco de dados
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

def create_table(sql):
    """
    Executa um comando SQL para criar uma tabela e confirma a transação.
    Fecha a conexão e o cursor após a operação.
    """
    conn = None # Inicializa conn fora do try para garantir que esteja definido
    cur = None  # Inicializa cur fora do try
    try:
        conn = conectar()
        if conn is None:
            return

        cur = conn.cursor()
        print("Executando o comando SQL para criar a tabela...")
        cur.execute(sql)
        conn.commit() # <<< ESSA LINHA É CRUCIAL! Confirma as alterações no banco de dados.
        print("Tabelas criadas com sucesso e transação confirmada.")
    except psycopg2.DatabaseError as error:
        print(f"Erro ao criar tabelas: {error}")
        # Se ocorrer um erro, é uma boa prática fazer um rollback
        if conn:
            conn.rollback()
        raise # Re-lança o erro para que ele possa ser tratado em outro lugar, se necessário
    finally:
        # Garante que o cursor e a conexão sejam fechados
        if cur:
            cur.close()
            print("Cursor fechado.")
        if conn:
            conn.close()
            print("Conexão com o banco de dados fechada.")

def teste():
    """
    Conecta ao banco de dados, busca e retorna as tabelas existentes para verificar.
    Fecha a conexão e o cursor após a operação.
    """
    conn = None
    cur = None
    try:
        conn = conectar()
        if conn is None:
            return []

        cur = conn.cursor()
        query_sql = """
        SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';
        """
        print("Buscando tabelas existentes para verificação...")
        cur.execute(query_sql)
        tables = cur.fetchall()
        print(f"Tabelas encontradas: {tables}")
        return tables
    except psycopg2.DatabaseError as error:
        print(f"Erro ao buscar tabelas: {error}")
        return []
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def criar_tabela_parlamentar():
    """Define o SQL para criar a tabela parlamentar e chama create_table."""
    sql = """
    CREATE TABLE IF NOT EXISTS parlamentar (
        id SERIAL PRIMARY KEY,
        mat_parlamentar INT NOT NULL,
        nome VARCHAR(100) UNIQUE NOT NULL,
        partido VARCHAR(100) NOT NULL,
        UF VARCHAR(100) NOT NULL,
        idLegislatura INT NOT NULL
    );"""
    print("Iniciando a criação da tabela 'parlamentar'.")
    create_table(sql)

# Execução principal
criar_tabela_parlamentar()
print("\nVerificando se a tabela foi criada:")
teste() # Chama teste para listar todas as tabelas, não apenas 'parlamentar'

