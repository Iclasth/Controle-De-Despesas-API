from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import schemas, repository
from app.db import get_db
from app.services import RegistroDespesa

router = APIRouter(prefix="/despesas", tags=["Despesas"])
relatorio_service = RegistroDespesa()

@router.post("/", response_model=schemas.DespesaOut, status_code=status.HTTP_201_CREATED)
def create_despesa(despesa: schemas.DespesaCreate, db: Session = Depends(get_db)):
    return repository.listar_despesas(db, skip=0, limit=100)

@router.get("/{id_despesa}", response_model=schemas.DespesaOut)
def get_despesa(id_despesa: int, db: Session = Depends(get_db)):
    despesa = repository.resgatar_despesa(db, id_despesa)
    if not despesa:
        raise HTTPException(status_code=404, detail="A despesa não foi encontrada")
    return despesa

@router.get("/", response_model=List[schemas.DespesaOut])
def list_despesas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repository.listar_despesas(db, skip, limit)

@router.put("/{id_despesa}", response_model=schemas.DespesaOut)
def update_despesa(id_despesa: int, updates: schemas.DespesaUpdate, db: Session = Depends(get_db)):
    data = updates.dict(exclude_unset=True)
    despesa_atualizada = repository.atualizar_despesa(db, id_despesa, data)
    if not despesa_atualizada:
        raise HTTPException(status_code=404, detail="A despesa não foi encontrada")
    return despesa_atualizada

@router.delete("/{id_despesa}", status_code=status.HTTP_204_NO_CONTENT)
def delete_despesa(id_despesa: int, db: Session = Depends(get_db)):
    sucesso = repository.deletar_despesa(db, id_despesa)
    if not sucesso:
        raise HTTPException(status_code=404, detail="A despesa não foi encontrada")
    return

@router.get("/relatorio/{ano}/{mes}")
def relatorio_despesas(ano: int, mes: int, db: Session = Depends(get_db)):
    despesas = db.query(repository.models.DespesaModel).all()
    relatorio = relatorio_service.gerar_relatorio(db, ano, mes)
    return {"ano": ano, "mes": mes, "relatorio": relatorio}