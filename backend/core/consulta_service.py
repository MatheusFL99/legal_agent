import re
from core.tools.jusbrasil_tool import tool_busca_jusbrasil
from core.tools.ia_tool import tool_ia_gerar_resposta
from core.tools.cache_tool import tool_verificar_historico, tool_buscar_respostas_similares
from core.tools.graph_rag_tool import tool_graph_rag_contexto
from urllib.parse import urlparse

def extrair_links(texto):
    padrao = r'https?://[^\s)>\"]+'
    return re.findall(padrao, texto)

def gerar_titulo_amigavel(link: str) -> str:
    dominio = urlparse(link).netloc.replace("www.", "")
    if "jusbrasil" in dominio:
        return "Jusbrasil"
    elif "planalto.gov.br" in dominio:
        return "Portal da Legislação (Planalto)"
    elif "senado.leg.br" in dominio:
        return "Senado Federal"
    elif "projuris.com.br" in dominio:
        return "Projuris"
    else:
        return f"Fonte: {dominio}"

def realizar_consulta(pergunta):
    resposta_cache, fontes_cache = tool_verificar_historico(pergunta)
    if resposta_cache:
        return {
            "answer": resposta_cache,
            "disclaimer": "Esta resposta é gerada por IA e não substitui a orientação de um advogado profissional.",
            "resources": fontes_cache or [],
        }

    fontes_externas = tool_busca_jusbrasil(pergunta)
    links_jusbrasil = [fonte['link'] for fonte in fontes_externas]

    contexto = tool_graph_rag_contexto(pergunta)
    respostas_similares = tool_buscar_respostas_similares(pergunta)

    contexto_completo = ""
    if contexto:
        contexto_completo += contexto + "\n\n"
    if respostas_similares:
        contexto_completo += respostas_similares

    resposta_ia = tool_ia_gerar_resposta(pergunta, links_jusbrasil, contexto=contexto_completo)

    links_ia = extrair_links(resposta_ia)
    fontes_encontradas = [{"titulo": gerar_titulo_amigavel(link), "link": link} for link in links_ia]

    return {
        "answer": resposta_ia,
        "disclaimer": "Esta resposta é gerada por IA e não substitui a orientação de um advogado profissional.",
        "resources": fontes_encontradas,
    }
