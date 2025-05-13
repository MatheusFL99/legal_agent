from core.mongodb import db
import json
from pathlib import Path

CATEGORIAS_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "categorias.json"
with open(CATEGORIAS_FILE, "r", encoding="utf-8") as f:
    categorias = json.load(f)

def extrair_tags(texto: str):
    texto = texto.lower()
    tags_encontradas = set()

    for palavras in categorias.values():
        for palavra in palavras:
            if palavra in texto:
                tags_encontradas.add(palavra)

    return list(tags_encontradas)

def tool_graph_rag_contexto(pergunta: str) -> str:
    tags = extrair_tags(pergunta)
    if not tags:
        return ""

    documento_principal = db.documentos_juridicos.find_one({"tags": {"$in": tags}})
    if not documento_principal:
        return ""

    referencias = documento_principal.get("referencias", [])
    documentos_relacionados = db.documentos_juridicos.find({"_id": {"$in": referencias}})

    trechos = [f"{documento_principal['titulo']}:\n{documento_principal['conteudo']}"]
    for doc in documentos_relacionados:
        trechos.append(f"{doc['titulo']}:\n{doc['conteudo']}")

    return "\n\n".join(trechos)
