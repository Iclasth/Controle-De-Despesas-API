from sqlalchemy import Column, Integer, String, Float, Date
from app.core.db import Base 

class Despesa(Base): 
    __tablename__ = "despesas"

    id_despesa = Column(Integer, primary_key=True, index=True)
    desc_despesa = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data_despesa = Column(Date, nullable= False)
    categoria = Column(String, nullable=True)
    tipo_despesa = Column(String, default="Variável")  