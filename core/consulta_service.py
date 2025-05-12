from core.tools.jusbrasil_tool import tool_busca_jusbrasil
from core.tools.ia_tool import tool_ia_gerar_resposta
from core.tools.cache_tool import tool_verificar_historico

def realizar_consulta(pergunta):
    # verificado se ja existe resposta no historico
    resposta_cache, fontes_cache = tool_verificar_historico(pergunta)
    if resposta_cache:
        return resposta_cache, fontes_cache

    # buscando e enviando para IA
    fontes = tool_busca_jusbrasil(pergunta)
    links = [fonte['link'] for fonte in fontes]
    resposta = tool_ia_gerar_resposta(pergunta, links)

    return resposta, fontes
