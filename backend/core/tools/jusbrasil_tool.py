from core.jusbrasil_search import buscar_legislacao_jusbrasil

def tool_busca_jusbrasil(pergunta: str) -> list:
    resultados = buscar_legislacao_jusbrasil(pergunta)
    return resultados[:5]
