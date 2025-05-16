from core.classifier import classificar_pergunta
from core.planner import Planner
from core.consulta_service import realizar_consulta
from core.historico_service import salvar_consulta_no_historico

def exibir_resultados(titulo, conteudo):
    print(titulo)
    print(f"{'='*len(titulo)}")

    if isinstance(conteudo, list):
        for item in conteudo:
            print(f"- {item['titulo']}: {item['link']}")
    else:
        print(conteudo)

def main():
    print("Bem-vindo ao Agente Jurídico!\n")
    planner = Planner()

    while True:
        try:
            pergunta = input("Digite sua pergunta jurídica (ou 'sair' para encerrar): ").strip()

            if pergunta.lower() == "sair":
                print("Encerrando o Agente Jurídico.")
                break

            plano = planner.planejar(pergunta)
            exibir_resultados("Plano de Ação Gerado", plano)

            categoria = classificar_pergunta(pergunta)
            exibir_resultados("Categoria Identificada", categoria)

            if plano.get("usar_ia", True):
                resultado = realizar_consulta(pergunta)
                exibir_resultados("Resposta da Inteligência Artificial", resultado["answer"])

                salvar_consulta_no_historico(
                    pergunta,
                    resultado["answer"],
                    resultado["resources"]
                )


        except Exception as e:
            print(f"\n[ERRO] Ocorreu um problema: {str(e)}\n")

if __name__ == "__main__":
    main()