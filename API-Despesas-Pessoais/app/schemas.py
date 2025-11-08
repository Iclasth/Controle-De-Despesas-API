from pydantic import BaseModel, Field, validator
from datetime import date
from typing import Optional

CATEGORIAS_PERMITIDAS = {"Alimentação, Transporte, Lazer, Saúde, Moradia, Outros"}

class DespesaBase(BaseModel):
    categoria: str
    valor: float = Field(..., gt=0, description="Valor da despesa não pode ser negativo.")
    data_despesa: date
    desc_despesa: Optional[str] = None
    tipo_despesa: Optional[str] = "Variável"

    @validator("categoria")
    def check_categoria(cls, value):
        if value not in CATEGORIAS_PERMITIDAS:
            raise ValueError(f"A categoria deve estar entre as categorias seguintes: {sorted(CATEGORIAS_PERMITIDAS)}")
        return value
    
    @validator("tipo_despesa")
    def check_tipo_despesa(cls, value):
        if value is None:
            return value
        if value not in {"Fixa", "Variável"}:
            raise ValueError("O tipo de despesa deve ser 'fixa' ou 'variavel'")
        
        return value
    
class DespesaCreate(DespesaBase):
    pass

class DespesaUpdate(BaseModel):
    categoria: Optional[str]
    valor: Optional[float]
    data_despesa: Optional[date]
    desc_despesa: Optional[str]
    tipo_despesa: Optional[str]

class DespesaOut(DespesaBase):
    id_despesa: int

    class Config:
        orm_mode = True