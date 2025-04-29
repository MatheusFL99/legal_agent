from core.mongodb import salvar_historico

def salvar_consulta_no_historico(pergunta, resposta_ia, fontes):
    salvar_historico(
        pergunta=pergunta,
        resposta=resposta_ia,
        fontes=fontes
    )
