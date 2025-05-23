import requests
import json
from config.settings import OPENROUTER_API_KEY

def perguntar_openrouter(mensagem_usuario, fontes=None, contexto="", historico=None):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt_inicial = (
        "You are an AI Legal Assistant. Your role is to answer basic legal questions or assist lawyers with legal-related tasks.\n"
        "You must ONLY answer questions related to legal matters. If the question is not related to law or legal tasks, you should politely decline to answer.\n"
        "Provide links to public legal resources to support your answer when appropriate.\n"
        "All responses must be written in Brazilian Portuguese and mainly based on Brasil.\n"
        "Do NOT include disclaimers directly in the main answer; these will be handled separately by the system.\n"
        
    )

    messages = [{"role": "system", "content": prompt_inicial}]

    if historico:
        for h in historico:
            role = "user" if h.role == "user" else "assistant"
            messages.append({
                "role": role,
                "content": h.content
            })

    if contexto:
        messages.append({
            "role": "system",
            "content": f"Contexto jurídico recuperado do banco de dados:\n{contexto}"
        })

    if fontes:
        links = "\n".join(f"- {link}" for link in fontes)
        messages.append({
            "role": "system",
            "content": f"Links relevantes para consulta:\n{links}"
        })

    # prompt final
    messages.append({"role": "user", "content": mensagem_usuario})

    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": messages
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except requests.HTTPError as e:
        raise Exception(f"[OpenRouter] Erro HTTP {response.status_code}: {response.text}")
    except requests.RequestException as e:
        raise Exception(f"[OpenRouter] Erro de conexão: {str(e)}")
