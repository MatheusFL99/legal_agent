def buscar_legislacao_jusbrasil(termo_busca):
    url_busca = f"https://www.jusbrasil.com.br/legislacao/busca?q={termo_busca.replace(' ', '+')}"
    resultados = [
        {"titulo": f"Busca por '{termo_busca}' no JusBrasil", "link": url_busca}
    ]
    return resultados
