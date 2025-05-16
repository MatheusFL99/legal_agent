from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.consulta_service import realizar_consulta
from core.historico_service import salvar_consulta_no_historico
from core.classifier import classificar_pergunta
from core.planner import Planner

app = FastAPI(title="Agente Jurídico - API")
planner = Planner()

class ConsultaInput(BaseModel):
    pergunta: str

class ConsultaOutput(BaseModel):
    answer: str
    disclaimer: str
    resources: list[dict]


@app.post("/consultar")
def consultar_legalmente(dados: ConsultaInput):
    try:
        categoria = classificar_pergunta(dados.pergunta)
        plano = planner.planejar(dados.pergunta)

        if plano.get("usar_ia", True):
            resultado = realizar_consulta(dados.pergunta)

            # Salvar no histórico com os campos esperados
            salvar_consulta_no_historico(
                dados.pergunta,
                resultado["answer"],
                resultado["resources"]
            )

            # Retornar tudo conforme o frontend espera
            return {
                "answer": resultado["answer"],
                "disclaimer": resultado["disclaimer"],
                "resources": resultado["resources"]
            }

        else:
            raise HTTPException(status_code=400, detail="Plano atual não permite uso da IA.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
