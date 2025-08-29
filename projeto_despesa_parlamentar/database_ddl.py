import database_conn as db_conn
import psycopg2

def create_table(sql):
    """
    Executa um comando SQL para criar uma tabela e confirma a transação.
    Fecha a conexão e o cursor após a operação.
    """
    conn = None # Inicializa conn fora do try para garantir que esteja definido
    cur = None  # Inicializa cur fora do try
    try:
        conn = db_conn.conectar()
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
