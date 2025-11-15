from sqlalchemy.orm import Session
from app import models, schemas
from datetime import date

def criar_despesa(db: Session, despesa: schemas.DespesaCreate):
    db_objeto = models.Despesa(
        categoria= despesa.categoria,
        valor= despesa.valor,
        data_despesa= despesa.data_despesa,
        desc_despesa= despesa.desc_despesa,
        tipo_despesa= despesa.tipo_despesa
    )
    db.add(db_objeto)
    db.commit()
    db.refresh(db_objeto)
    return db_objeto

def resgatar_despesa(db: Session, id_despesa: int):
    return db.query(models.Despesa).filter(models.Despesa.id_despesa == id_despesa).first()

def listar_despesas(db: Session, skip: int = 0, limit: int = 100 ):
    return db.query(models.Despesa).offset(skip).limit(limit).all()

def atualizar_despesa(db: Session, id_despesa: int, updates: dict):
    objeto_despesa = resgatar_despesa(db, id_despesa)
    if not objeto_despesa:
        return None
    for key, value in updates.items():
        setattr(objeto_despesa, key, value)
    db.commit()
    db.refresh(objeto_despesa)
    return objeto_despesa

def deletar_despesa(db: Session, id_despesa: int):
    objeto_despesa = resgatar_despesa(db, id_despesa)
    if not objeto_despesa:
        return False
    db.delete(objeto_despesa)
    db.commit()
    return True




