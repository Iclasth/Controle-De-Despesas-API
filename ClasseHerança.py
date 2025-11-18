class Despesa:
    def __init__(self, valor, categoria, data):
        self.valor = valor
        self.categoria = categoria
        self.data = data

    def info(self):
        return f"{self.categoria} - R$ {self.valor} em {self.data}"


class DespesaFixa(Despesa):
    def __init__(self, valor, categoria, data, descricao):
        super().__init__(valor, categoria, data)
        self.descricao = descricao

    def calcular_anual(self):
        return self.valor * 12

class DespesaVariavel(Despesa):
    def __init__(self, valor, categoria, data, observacao=None):
        super().__init__(valor, categoria, data)
        self.observacao = observacao

    def resumo(self):
        if self.observacao:
            return f"{self.categoria}: R$ {self.valor} ({self.observacao})"
        return f"{self.categoria}: R$ {self.valor}"


























