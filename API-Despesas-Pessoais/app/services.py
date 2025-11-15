from abc import ABC, abstractmethod
from datetime import date
from typing import List, Dict
from app.models import Despesa

class RegistroFinanceiro(ABC):
    @abstractmethod
    def gerar_relatorio_mensal(self, despesas: List[Despesa], mes:int, ano: int) -> Dict[str, float]:
        pass

class Despesa:
    def __init__(self, valor: float, categoria: str, data_despesa: date, desc_despesa: str = None):

        self.valor = valor
        self.categoria = categoria
        self.data_despesa = data_despesa
        self.desc_despesa = desc_despesa

def calcular_valor_mensal(self) -> float:
    return self.valor

class Despesafixa(Despesa):
    def calcular_valor_mensal(self) -> float:
        return self.valor 
    
class Despesavariavel(Despesa):
    def calcular_valor_mensal(self) -> float:
        return self.valor  

class RegistroDespesa(RegistroFinanceiro):
    def gerar_relatorio_mensal(self, despesas: List[Despesa], mes: int, ano: int):
        relatorio= {}
        for d in despesas:
            if d.data.month == mes and d.data.year == ano:
                relatorio.setdefault(d.categoria, 0)
                relatorio[d.categoria] += d.valor
        return relatorio
        

# def map_model_to_domain(model):
#     if model.tipo_despesa == "Fixa":
#         return Despesafixa
#     if model.tipo_despesa == "Variável":
#         return Despesavariavel
    