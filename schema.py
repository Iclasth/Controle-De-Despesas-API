from pydantic import BaseModel
from typing import Optional

class CriarDespesa(BaseModel):
    numero_id: int
    valor_da_despesa: float
    categoria: str
    descricao_despesa: str
    tipo_despesa: str
