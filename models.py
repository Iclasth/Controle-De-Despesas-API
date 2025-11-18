from sqlalchemy  import create_engine,Column,String,Float,Integer,Date
from sqlalchemy.orm import declarative_base

db= create_engine("sqlite:///banco.db")
Base = declarative_base()

# Criar as classes/tabelas do banco
class Despesa(Base):
    __tablename__="Despesas"

    id= Column(Integer, primary_key=True, autoincrement=True)
    valor= Column(Float)
    categoria=Column(String)
    descricao=Column(String)
    data= Column(Date, nullable=False)
    tipo_de_despesa=Column(String)

def __init__(self,valor,categoria,descricao,data,tipo_de_despesa):
    self.valor=valor
    self.categoria=categoria
    self.descricao=descricao
    self.data=data
    self.tipo_de_despesa=tipo_de_despesa
    

# valor 
# categoria
# descricao
# id
# deta 
# tipo de despesa
# executa a criação dos metadados do seu banco(criar efetivamente o banco de dados)