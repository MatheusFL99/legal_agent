import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CATEGORIAS_FILE = BASE_DIR / 'data' / 'categorias.json'

with open(CATEGORIAS_FILE, 'r', encoding='utf-8') as f:
    categorias = json.load(f)

def limpar_texto(texto: str) -> str:
    
    # removendo caracteres especiais e deixa o texto minusculo
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z0-9áéíóúãõâêîôûç\s]', '', texto)  # mantem letras acentuadas
    return texto

def classificar_pergunta(pergunta: str) -> str:
    pergunta_limpa = limpar_texto(pergunta)

    for categoria, palavras_chave in categorias.items():
        for palavra in palavras_chave:
            if palavra in pergunta_limpa:
                return categoria

    return "pergunta_geral"

# teste
if __name__ == "__main__":
    pergunta = input("Digite uma pergunta: ")
    categoria_detectada = classificar_pergunta(pergunta)
    print(f"Categoria detectada: {categoria_detectada}")

