import api_dados_abertos as api
import json
import database_conn as db_conn
import psycopg2

def seed_parlamentares():
     data = api.get_parlamentares()

     insert_sql = """
          INSERT INTO parlamentar (
          mat_parlamentar,
          nome,
          partido,
          uf,
          idlegislatura
          ) VALUES (%s, %s, %s, %s, %s)
          ON CONFLICT (nome) DO NOTHING;
     """
     # A cláusula ON CONFLICT (nome) DO NOTHING evita erros se você tentar inserir dados já existentes.
     # Substituí 'id' por 'nome' como a coluna com o UNIQUE, pois o id é um serial. Se houver outro critério único, altere a coluna

     
     for parlamentar in data:
          matricula = parlamentar['id']
          nome = parlamentar['nome']
          partido = parlamentar['siglaPartido']
          uf = parlamentar['siglaUf']
          idLegislatura = parlamentar['idLegislatura']

def get_total_despesas(matricula):
     despesas_list = api.get_despesas(matricula)
     total_gastos = 0
     for despesa in despesas_list:
          total_gastos += despesa.get("valorLiquido", 0)
     print(total_gastos)

get_total_despesas(204528)