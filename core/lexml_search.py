import requests
from bs4 import BeautifulSoup

def buscar_lexml(termo_busca):
    """
    Realiza uma busca no LexML usando o termo fornecido.

    Args:
        termo_busca (str): Palavra ou frase para buscar.

    Returns:
        list: Lista de dicionários com título e link dos resultados encontrados.

    Raises:
        Exception: Se ocorrer erro na busca ou no processamento dos dados.
    """
    
    # Monta a URL de busca
    url = f"https://www.lexml.gov.br/busca/search?keyword={termo_busca.replace(' ', '+')}"
    
    try:
        # Faz a requisição HTTP
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida
        if response.status_code != 200:
            raise Exception(f"Erro ao buscar no LexML: {response.status_code}")

        # Faz o parser do HTML retornado
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra todos os resultados da busca (ajustar conforme HTML real do site)
        resultados = []
        for item in soup.select('.documentSummary'):
            titulo_element = item.select_one('.title')
            link_element = item.select_one('a')

            if titulo_element and link_element:
                titulo = titulo_element.text.strip()
                link = link_element['href']
                resultados.append({'titulo': titulo, 'link': link})

        return resultados if resultados else [{"titulo": "Nenhum resultado encontrado.", "link": ""}]

    except Exception as e:
        raise Exception(f"Erro ao buscar no LexML: {str(e)}")
