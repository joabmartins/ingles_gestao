import database_conn as db_conn
import psycopg2

def get_parlamentar():
    """
    Conecta ao banco de dados, busca e retorna as tabelas existentes para verificar.
    Fecha a conexão e o cursor após a operação.
    """
    conn = None
    cur = None
    try:
        conn = db_conn.conectar()
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

get_parlamentar() # Chama teste para listar todas as tabelas, não apenas 'parlamentar'