from core.jusbrasil_search import buscar_legislacao_jusbrasil
from api.openrouter_api import perguntar_openrouter

def realizar_consulta(pergunta):
    resultados_jusbrasil = buscar_legislacao_jusbrasil(pergunta)
    

    resultados_jusbrasil = resultados_jusbrasil[:5]    
    fontes_links = [item['link'] for item in resultados_jusbrasil]
    resposta_ia = perguntar_openrouter(pergunta, fontes_links)

    return resposta_ia, resultados_jusbrasil