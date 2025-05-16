import requests
import json
from config.settings import OPENROUTER_API_KEY

def perguntar_openrouter(mensagem_usuario, fontes=None, contexto=""):

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        'You are an AI Legal Assistant. Your role is to answer basic legal questions or assist lawyers with legal-related tasks. '
        'You must ONLY answer questions related to legal matters. If the question is not related to law or legal tasks, you should politely decline to answer.'
        'Provide links to public legal resources to support your answer when appropriate. '
        'All responses must be written in Brazilian Portuguese and mainly based on Brasil. '
        'Question: {{{question}}}'
    )

    if contexto:
        prompt += f"Contexto jurídico recuperado do banco de dados:\n{contexto}\n\n"

    if fontes:
        links = "\n".join(f"- {link}" for link in fontes)
        prompt += f"Links relevantes para consulta:\n{links}\n\n"

    prompt += f"Pergunta: {mensagem_usuario}"

    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            raise Exception(f"[OpenRouter] Erro {response.status_code}: {response.text}")
    except requests.RequestException as e:
        raise Exception(f"[OpenRouter] Erro de conexão: {str(e)}")
