from fastapi import APIRouter,Depends
from sqlalchemy.orm import sessionmaker
from models import db
from dependences import pegar_sessao
from models import Base
from schema import CriarDespesa


despesa_router = APIRouter(prefix="/despesas", tags=["Despesas"])


@despesa_router.post("/criar")
async def criar_despesa(criar_despesa:CriarDespesa, session=Depends(pegar_sessao)):
    Session = sessionmaker(bind=db)
    session = Session()
    despesa=despesa(CriarDespesa.id,CriarDespesa.tipo_despesa,CriarDespesa.categoria,CriarDespesa.descricao_despesa,CriarDespesa.tipo_despesa)
    session.add(despesa)
    session.commit()
    


    
    return {"mensagem": "Você acessou a área para criar despesas"}


@despesa_router.get("/buscar_uma")
async def buscar_uma_despesa(id: int):
  return {"id"(id)}

@despesa_router.get("/buscar_todas")
async def buscar_todas_as_despesa():
    return {"mensagem": "Você acessou a área para buscar todas as despesas"}
@despesa_router.patch ("/editar_despesa")
async def editar_despesa():
    return{"Você pode editar uma despesa"}
@despesa_router.delete("/deletar")
async def deletar_despesa():
    return{"Você pode deletar uma despesa"}
