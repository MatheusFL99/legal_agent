from core.mongodb import collection
from difflib import SequenceMatcher

def tool_verificar_historico(pergunta: str):
    doc = collection.find_one({"pergunta": pergunta})
    if doc:
        return doc["resposta_ia"], doc.get("fontes_encontradas", [])
    return None, None

def tool_buscar_respostas_similares(pergunta: str, limite: int = 2) -> str:
    historico = collection.find({}, {"pergunta": 1, "resposta_ia": 1}).limit(50)

    similares = []
    for doc in historico:
        similaridade = SequenceMatcher(None, pergunta.lower(), doc["pergunta"].lower()).ratio()
        if similaridade >= 0.6:
            similares.append((similaridade, doc["resposta_ia"]))

    similares.sort(reverse=True)
    respostas = [f"Resposta anterior relacionada:\n{res}" for _, res in similares[:limite]]

    return "\n\n".join(respostas) if respostas else ""
