import json
import re
from pathlib import Path

# Caminho para o arquivo categorias.json
BASE_DIR = Path(__file__).resolve().parent.parent
CATEGORIAS_FILE = BASE_DIR / 'data' / 'categorias.json'

# Carregar as categorias uma vez
with open(CATEGORIAS_FILE, 'r', encoding='utf-8') as f:
    categorias = json.load(f)

def limpar_texto(texto: str) -> str:
    """
    Remove caracteres especiais e deixa o texto minúsculo para facilitar a análise.
    """
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z0-9áéíóúãõâêîôûç\s]', '', texto)  # Mantém letras acentuadas
    return texto

def classificar_pergunta(pergunta: str) -> str:
    """
    Analisa a pergunta e retorna a categoria correspondente.
    Se não encontrar nada, retorna 'pergunta_geral' como padrão.
    """
    pergunta_limpa = limpar_texto(pergunta)

    for categoria, palavras_chave in categorias.items():
        for palavra in palavras_chave:
            if palavra in pergunta_limpa:
                return categoria

    # Se nenhuma palavra-chave for encontrada, assume pergunta geral
    return "pergunta_geral"

# Para testes rápidos
if __name__ == "__main__":
    pergunta = input("Digite uma pergunta: ")
    categoria_detectada = classificar_pergunta(pergunta)
    print(f"Categoria detectada: {categoria_detectada}")
    
