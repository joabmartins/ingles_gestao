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
        print("Conexão com o banco de dados estabelecida com sucesso.")
        return conn
    except psycopg2.DatabaseError as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None

def criar_tabelas(cur):
    """Cria as tabelas 'alunos', 'disciplinas' e 'alunos_disciplinas'."""
    create_tables_sql = """
    -- Tabela de Alunos
    CREATE TABLE IF NOT EXISTS alunos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        matricula VARCHAR(20) UNIQUE NOT NULL
    );

    -- Tabela de Disciplinas
    CREATE TABLE IF NOT EXISTS disciplinas (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL
    );

    -- Tabela de relacionamento entre Alunos e Disciplinas
    CREATE TABLE IF NOT EXISTS alunos_disciplinas (
        aluno_id INT REFERENCES alunos(id) ON DELETE CASCADE,
        disciplina_id INT REFERENCES disciplinas(id) ON DELETE CASCADE,
        PRIMARY KEY (aluno_id, disciplina_id)
    );
    """
    try:
        cur.execute(create_tables_sql)
        print("Tabelas criadas com sucesso.")
    except psycopg2.DatabaseError as error:
        print(f"Erro ao criar tabelas: {error}")
        raise

def popular_dados(cur):
    """Popula as tabelas com dados de exemplo."""
    populate_data_sql = """
    -- Insere alunos
    INSERT INTO alunos (nome, matricula) VALUES
    ('João Silva', '2023001') ON CONFLICT (matricula) DO NOTHING;

    INSERT INTO alunos (nome, matricula) VALUES
    ('Maria Santos', '2023002') ON CONFLICT (matricula) DO NOTHING;

    -- Insere disciplinas
    INSERT INTO disciplinas (nome) VALUES
    ('Matemática') ON CONFLICT DO NOTHING;

    INSERT INTO disciplinas (nome) VALUES
    ('História') ON CONFLICT DO NOTHING;

    INSERT INTO disciplinas (nome) VALUES
    ('Física') ON CONFLICT DO NOTHING;

    -- Relaciona alunos e disciplinas
    INSERT INTO alunos_disciplinas (aluno_id, disciplina_id) VALUES
    ((SELECT id FROM alunos WHERE nome = 'João Silva'), (SELECT id FROM disciplinas WHERE nome = 'Matemática')),
    ((SELECT id FROM alunos WHERE nome = 'João Silva'), (SELECT id FROM disciplinas WHERE nome = 'Física')),
    ((SELECT id FROM alunos WHERE nome = 'Maria Santos'), (SELECT id FROM disciplinas WHERE nome = 'História'))
    ON CONFLICT DO NOTHING;
    """
    try:
        cur.execute(populate_data_sql)
        print("Dados populados com sucesso.")
    except psycopg2.DatabaseError as error:
        print(f"Erro ao popular dados: {error}")
        raise

def buscar_disciplinas_aluno(cur, nome_aluno):
    """Busca e retorna as disciplinas em que um aluno está matriculado."""
    query_sql = """
    SELECT
        d.nome
    FROM
        alunos_disciplinas AS ad
    JOIN
        alunos AS a ON ad.aluno_id = a.id
    JOIN
        disciplinas AS d ON ad.disciplina_id = d.id
    WHERE
        a.nome = %s;
    """
    try:
        cur.execute(query_sql, (nome_aluno,))
        return cur.fetchall()
    except psycopg2.DatabaseError as error:
        print(f"Erro ao buscar disciplinas: {error}")
        return []

def main():
    """Orquestra a execução de todas as operações no banco de dados."""
    conn = conectar()
    if conn is None:
        return

    cur = conn.cursor()
    try:
        criar_tabelas(cur)
        popular_dados(cur)
        
        # Faz a busca por um aluno específico
        aluno_nome_busca = 'João Silva'
        disciplinas = buscar_disciplinas_aluno(cur, aluno_nome_busca)

        print(f"\nDisciplinas em que o aluno '{aluno_nome_busca}' está matriculado:")
        if disciplinas:
            for row in disciplinas:
                print(f"- {row[0]}")
        else:
            print("Nenhuma disciplina encontrada.")
        
        # Comita as alterações no banco de dados
        conn.commit()

    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
        # Desfaz as alterações em caso de erro
        conn.rollback()

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("\nConexão com o banco de dados encerrada.")

if __name__ == '__main__':
    main()