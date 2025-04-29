from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client["agente_juridico"]
collection = db["historico"]

def salvar_historico(*, pergunta, resposta, fontes):
    try:
        documento = {
            "pergunta": pergunta,
            "resposta_ia": resposta,
            "fontes_encontradas": fontes,
            "data_hora": datetime.now()
        }
        collection.insert_one(documento)
        print("[MONGODB] Pergunta, resposta e fontes salvas com sucesso!")
    except Exception as e:
        print(f"[MONGODB][ERRO] Falha ao salvar histórico: {str(e)}")
