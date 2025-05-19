from core.mongodb import salvar_historico

def tool_salvar_historico(pergunta: str, resposta: str, fontes: list[dict]):
    salvar_historico(pergunta=pergunta, resposta=resposta, fontes=fontes)
