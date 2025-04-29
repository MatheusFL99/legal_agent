import requests
import json
from config.settings import OPENROUTER_API_KEY

def perguntar_openrouter(mensagem_usuario: str, fontes: list = None) -> str:
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt_usuario = mensagem_usuario 
    if fontes:
        prompt_usuario += "\n\nConsidere também estas fontes como base para sua resposta:\n"
        for fonte in fontes:
            prompt_usuario += f"- {fonte}\n"

    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um assistente jurídico. "
                    "Responda APENAS perguntas jurídicas com linguagem clara e objetiva. "
                    "Sempre avise que sua resposta não substitui a orientação de um advogado. "
                    "Use sempre o idioma Português (Brasil) e garanta que toda resposta esteja traduzida."
                )
            },
            {
                "role": "user",
                "content": prompt_usuario
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            raise Exception(f"Erro na OpenRouter API: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        raise Exception(f"Erro de conexão com a OpenRouter API: {str(e)}")
