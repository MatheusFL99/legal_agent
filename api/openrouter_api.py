import requests
import json
from config.settings import OPENROUTER_API_KEY

def perguntar_openrouter(mensagem_usuario, fontes=None, contexto=""):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt_base = (
       "You are a legal assistant trained to answer questions in a clear, objective, and technical manner. "
        "Respond ONLY to legal questions. All responses must be written in Brazilian Portuguese. "
        "Always include a disclaimer stating that your response does not replace the guidance of a qualified lawyer. "
        "If the question is not legal in nature, politely decline to answer.\n\n"
    )

    if contexto:
        prompt_base += f"Context extracted from database:\n{contexto}\n\n"

    if fontes:
        fontes_texto = "\n".join(f"- {link}" for link in fontes)
        prompt_base += f"External search fonts:\n{fontes_texto}\n\n"

    prompt_base += f"Question: {mensagem_usuario}"

    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "system", "content": prompt_base}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Erro na OpenRouter API: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        raise Exception(f"Erro de conexão com a OpenRouter API: {str(e)}")
