import requests
import json

# Acesse o site: Vá até o site do provedor da API (por exemplo, imdb-api.com).
# Crie uma conta: Faça um cadastro rápido, geralmente gratuito.
# Obtenha a chave: No painel de controle da sua conta, você encontrará uma seção para a "API Key" ou "Credenciais". Copie a chave que eles gerarem para você.
# Use no código: No seu código Python, você substitui o valor de exemplo (k_12345678) pela sua chave.
# Python
# Seu código Python
# api_key = 'SUA_CHAVE_DE_API_AQUI'
# url = f'https://imdb-api.com/en/API/Search/{api_key}/inception'

# https://publicapi.dev

# Exemplo usando a API de países
# url = 'https://restcountries.com/v3.1/all'
url = 'https://restcountries.com/v3.1/all?fields=name,capital,languages,population,area,continents,independent'
language_url = 'https://restcountries.com/v3.1/lang/spanish'

'''
{
    "id": 220560,
    "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/220560",
    "nome": "Thiago de Joaldo",
    "siglaPartido": "PP",
    "uriPartido": "https://dadosabertos.camara.leg.br/api/v2/partidos/37903",
    "siglaUf": "SE",
    "idLegislatura": 57,
    "urlFoto": "https://www.camara.leg.br/internet/deputado/bandep/220560.jpg",
    "email": "dep.thiagodejoaldo@camara.leg.br"
},
'''
dados_abertos_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'

'''
{
    "ano": 2025,
    "mes": 6,
    "tipoDespesa": "MANUTEN\u00c7\u00c3O DE ESCRIT\u00d3RIO DE APOIO \u00c0 ATIVIDADE PARLAMENTAR",
    "codDocumento": 7933669,
    "tipoDocumento": "Nota Fiscal Eletr\u00f4nica",
    "codTipoDocumento": 4,
    "dataDocumento": "2025-06-17T00:00:00",
    "numDocumento": "6654",
    "valorDocumento": 394.4,
    "urlDocumento": "http://www.camara.leg.br/cota-parlamentar/nota-fiscal-eletronica?ideDocumentoFiscal=7933669",
    "nomeFornecedor": "WMS COMERCIO DE ARTIGOS DE PAPELARIA LTDA",
    "cnpjCpfFornecedor": "12132854000100",
    "valorLiquido": 394.4,
    "valorGlosa": 0.0,
    "numRessarcimento": "",
    "codLote": 2146432,
    "parcela": 0
},
'''
despesa_exemplo = 'https://dadosabertos.camara.leg.br/api/v2/deputados/220560/despesas'

response = requests.get(despesa_exemplo)

if response.status_code == 200:
    data = response.json()
    print("Dados JSON recebidos com sucesso!")
    # Aqui você pode começar a processar e salvar os dados no seu banco de dados
    # Por exemplo: print(json.dumps(data[0], indent=2)) para ver um item
    # print(json.dumps(data[0], indent=2))
    print(json.dumps(data, indent=2))
else:
    print(f"Erro ao buscar os dados: {response.status_code}")