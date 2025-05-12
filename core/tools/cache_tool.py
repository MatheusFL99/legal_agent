from core.mongodb import collection

def tool_verificar_historico(pergunta: str):
    resultado = collection.find_one({"pergunta": pergunta})
    if resultado:
        print("[CACHE] Resposta encontrada no histórico.")
        return resultado["resposta_ia"], resultado["fontes_encontradas"]
    return None, None
