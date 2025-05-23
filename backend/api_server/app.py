import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from core.consulta_service import realizar_consulta
from core.historico_service import salvar_consulta_no_historico
from core.planner import Planner

app = FastAPI(title="Agente Jurídico - API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

planner = Planner()

class MensagemAnterior(BaseModel):
    role: str  
    content: str

class ConsultaInput(BaseModel):
    pergunta: str
    historico: Optional[List[MensagemAnterior]] = []

class ConsultaOutput(BaseModel):
    answer: str
    disclaimer: str
    resources: list[dict]


@app.post("/consultar")
def consultar_legalmente(dados: ConsultaInput):
    try:
        plano = planner.planejar(dados.pergunta)

        if plano.get("usar_ia", True):
            resultado = realizar_consulta(dados.pergunta, dados.historico)

            # salvar historico
            salvar_consulta_no_historico(
                dados.pergunta,
                resultado["answer"],
                resultado["resources"]
            )

            # retornar resultado
            print(resultado)
            return {
                "answer": resultado["answer"],
                "disclaimer": resultado["disclaimer"],
                "resources": resultado["resources"]
            }
        
            

        else:
            raise HTTPException(status_code=400, detail="Plano atual não permite uso da IA.")

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
