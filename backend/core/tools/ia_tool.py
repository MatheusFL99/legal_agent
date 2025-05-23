from api.openrouter_api import perguntar_openrouter

def tool_ia_gerar_resposta(pergunta: str, fontes: list[str], contexto: str = "", historico=None) -> str:
    return perguntar_openrouter(pergunta, fontes, contexto, historico)
