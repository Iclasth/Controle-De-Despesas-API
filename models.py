from sqlalchemy import Column, Integer, String, Float, Date
from application.core.database import Base

class DespesaDB(Base):

    _tablename_ = 'despesas'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    valor = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    data = Column(Date, nullable=False)
    descricao = Column(String, nullable=False)
    tipo_despesa = Column(String, nullable=False)