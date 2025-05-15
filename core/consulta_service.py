from core.tools.jusbrasil_tool import tool_busca_jusbrasil
from core.tools.ia_tool import tool_ia_gerar_resposta
from core.tools.cache_tool import tool_verificar_historico, tool_buscar_respostas_similares
from core.tools.graph_rag_tool import tool_graph_rag_contexto

def realizar_consulta(pergunta):
    # verificando se já existe resposta no histórico
    resposta_cache, fontes_cache = tool_verificar_historico(pergunta)
    if resposta_cache:
        return resposta_cache, fontes_cache

    fontes = tool_busca_jusbrasil(pergunta)
    links = [fonte['link'] for fonte in fontes]

    # recupera contexto e historico do mongo
    contexto_rag = tool_graph_rag_contexto(pergunta)
    respostas_similares = tool_buscar_respostas_similares(pergunta)

    contexto_completo = ""
    if contexto_rag:
        contexto_completo += contexto_rag + "\n\n"
    if respostas_similares:
        contexto_completo += respostas_similares

    if contexto_completo:
        resposta = tool_ia_gerar_resposta(pergunta, links, contexto=contexto_completo)
    else:
        resposta = tool_ia_gerar_resposta(pergunta, links)

    return resposta, fontes
