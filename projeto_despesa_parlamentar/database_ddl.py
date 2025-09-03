import database_conn as db_conn
import psycopg2

def create_table(sql):
    """
    Executa um comando SQL para criar uma tabela e confirma a transação.
    Fecha a conexão e o cursor após a operação.
    """
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
    finally:
        # Garante que o cursor e a conexão sejam fechados
        if conn:
            cur.close()
            conn.close()

def criar_tabela_parlamentar():
    """Define o SQL para criar a tabela parlamentar e chama create_table."""
    sql = """
    CREATE TABLE IF NOT EXISTS parlamentar (
        id SERIAL PRIMARY KEY,
        mat_parlamentar UNIQUE INT NOT NULL,
        nome VARCHAR(100) NOT NULL,
        partido VARCHAR(100) NOT NULL,
        UF VARCHAR(100) NOT NULL,
        total_gastos NUMERIC(10, 2),
    );"""
    print("Iniciando a criação da tabela 'parlamentar'.")
    create_table(sql)

def criar_tabela_despesa():
    """Define o SQL para criar a tabela parlamentar e chama create_table."""
    sql = """
    CREATE TABLE IF NOT EXISTS despesa (
        id SERIAL PRIMARY KEY,
        ano INT,
        mes INT,
        tipo_despesa TEXT,
        cod_documento INT,
        data_documento TIMESTAMP,
        num_documento VARCHAR(255),
        valor_documento NUMERIC(10, 2),
        nome_fornecedor VARCHAR(255),
        cnpj_cpf_fornecedor VARCHAR(20),
        valor_liquido NUMERIC(10, 2),
        id_parlamentar INT,
        FOREIGN KEY (id_parlamentar) REFERENCES parlamentar(id)
    );"""
    print("Iniciando a criação da tabela 'parlamentar'.")
    create_table(sql)

# Execução principal
criar_tabela_parlamentar()
criar_tabela_despesa()
