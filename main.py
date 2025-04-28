from core.classifier import classificar_pergunta
from core.lexml_search import buscar_lexml
from api.openrouter_api import perguntar_openrouter

def exibir_resultados(titulo, conteudo):
    print(f"\n{'='*len(titulo)}")
    print(titulo)
    print(f"{'='*len(titulo)}")

    if isinstance(conteudo, list):
        for item in conteudo:
            print(f"- {item['titulo']}: {item['link']}")
    else:
        print(conteudo)

def main():
    print("Bem-vindo ao Agente Jurídico!\n")
    
    while True:
        try:
            pergunta = input("Digite sua pergunta jurídica (ou 'sair' para encerrar): ").strip()

            if pergunta.lower() == "sair":
                print("Encerrando o Agente Jurídico. Até logo!")
                break

            # Classificar a pergunta
            categoria = classificar_pergunta(pergunta)
            exibir_resultados("Categoria Identificada", categoria)

            '''
            # Buscar no LexML se for um assunto jurídico reconhecido
            if categoria != "Desconhecido":
                resultados_lexml = buscar_lexml(pergunta)
                exibir_resultados("Resultados encontrados no LexML", resultados_lexml)
            else:
                print("\nCategoria não identificada. Pulando busca no LexML.")
            '''

            # Consultar a IA para resposta complementar
            resposta_ia = perguntar_openrouter(pergunta)
            exibir_resultados("Resposta da Inteligência Artificial", resposta_ia)
            

        except Exception as e:
            print(f"\n[ERRO] Ocorreu um problema: {str(e)}\n")

if __name__ == "__main__":
    main()