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
    pergunta: str
    categoria: str
    resposta: str
    fontes: list

@app.post("/consultar", response_model=ConsultaOutput)
def consultar_legalmente(dados: ConsultaInput):
    try:
        categoria = classificar_pergunta(dados.pergunta)
        plano = planner.planejar(dados.pergunta)

        if plano.get("usar_ia", True):
            resposta, fontes = realizar_consulta(dados.pergunta)
            salvar_consulta_no_historico(dados.pergunta, resposta, fontes)

            return ConsultaOutput(
                pergunta=dados.pergunta,
                categoria=categoria,
                resposta=resposta,
                fontes=fontes
            )
        else:
            raise HTTPException(status_code=400, detail="Plano atual não permite uso da IA.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
