import requests
import json
from config.settings import OPENROUTER_API_KEY

def perguntar_openrouter(mensagem_usuario):
    """
    Envia uma pergunta para o modelo de IA via OpenRouter API
    e retorna a resposta gerada.

    Args:
        mensagem_usuario (str): Texto da pergunta feita pelo usuário.

    Returns:
        str: Resposta gerada pela IA.

    Raises:
        Exception: Se ocorrer algum erro na comunicação com a API.
    """
    
    # URL do endpoint da OpenRouter
    url = "https://openrouter.ai/api/v1/chat/completions"

    # Autenticação
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    # Corpo da requisição: qual modelo usar e qual a mensagem
    payload = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um assistente jurídico. Responda APENAS perguntas jurídicas com linguagem clara e objetiva. Sempre avise que sua resposta não substitui a orientação de um advogado. Use sempre o idioma Protuguês Brasil. " 
                )
            },
            {
                "role": "user",
                "content": mensagem_usuario
            }
        ]
    }


    try:
        # Requisição
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Erro na OpenRouter API: {response.status_code} - {response.text}")

    except requests.RequestException as e:
        raise Exception(f"Erro de conexão com a OpenRouter API: {str(e)}")
