from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import schemas
from app.db.repository import criar_despesa, resgatar_despesa, listar_despesas, atualizar_despesa, deletar_despesa, models
from app.core.db import get_db
from app.services.services import RegistroDespesa

router = APIRouter(prefix="/despesas", tags=["Despesas"])
relatorio_service = RegistroDespesa()

@router.post("/", response_model=schemas.DespesaOut, status_code=status.HTTP_201_CREATED)
def create_despesa(despesa: schemas.DespesaCreate, db: Session = Depends(get_db)):
    nova_despesa = criar_despesa(db, despesa)
    return nova_despesa

@router.get("/{id_despesa}", response_model=schemas.DespesaOut)
def get_despesa(id_despesa: int, db: Session = Depends(get_db)):
    despesa = resgatar_despesa(db, id_despesa)
    if not despesa:
        raise HTTPException(status_code=404, detail="A despesa não foi encontrada")
    return despesa

@router.get("/", response_model=List[schemas.DespesaOut])
def list_despesas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return listar_despesas(db, skip, limit)

@router.put("/{id_despesa}", response_model=schemas.DespesaOut)
def update_despesa(id_despesa: int, updates: schemas.DespesaUpdate, db: Session = Depends(get_db)):
    data = updates.dict(exclude_unset=True)
    despesa_atualizada = atualizar_despesa(db, id_despesa, data)
    if not despesa_atualizada:
        raise HTTPException(status_code=404, detail="A despesa não foi encontrada")
    return despesa_atualizada

@router.delete("/{id_despesa}", status_code=status.HTTP_204_NO_CONTENT)
def delete_despesa(id_despesa: int, db: Session = Depends(get_db)):
    sucesso = deletar_despesa(db, id_despesa)
    if not sucesso:
        raise HTTPException(status_code=404, detail="A despesa não foi encontrada")
    return

# @router.get("/relatorio/{ano}/{mes}")
# def relatorio_despesas(ano: int, mes: int, db: Session = Depends(get_db)):
#     despesas = db.query(models.Despesa).all()
#     relatorio = relatorio_service.gerar_relatorio(db, ano, mes)
#     return {"ano": ano, "mes": mes, "relatorio": relatorio}


@router.get("/relatorio/{ano}/{mes}")
def relatorio_despesas(ano: int, mes: int, db: Session = Depends(get_db)):
    despesas = db.query(models.Despesa).all()

    
    
    relatorio = {}
    for d in despesas:
        if d.data_despesa.month == mes and d.data_despesa.year == ano:
            relatorio.setdefault(d.categoria, 0)
            relatorio[d.categoria] += d.valor

    if not relatorio:
        raise HTTPException(status_code=404, detail="Não existe despesas para esse periodo")
            
    return {"ano": ano, "mes": mes, "relatorio": relatorio}




