class Planner:
    def __init__(self):
        self.palavras_chave_jusbrasil = [
            "lei", "artigo", "constituição", "clt", "estatuto", "código", "norma",
            "jurisprudência", "sentença", "acórdão", "decisão", "tribunal", "legislação"
        ]

    def planejar(self, problema: str) -> dict:
        problema = problema.lower()

        acoes = {
            "consultar_jusbrasil": any(palavra in problema for palavra in self.palavras_chave_jusbrasil),
            "usar_ia": True
        }

        return acoes

# Teste
if __name__ == "__main__":
    planner = Planner()
    pergunta = input("Digite sua pergunta: ")
    plano = planner.planejar(pergunta)
    print("Plano: ", plano)