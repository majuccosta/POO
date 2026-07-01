class Relogio (object):
    def __init__(self,modelo,valor,ano):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def get_valor(self):
        return self.valor

    def set_modelo(self, novo_modelo: str):
        if type (novo_modelo) == str:
            self.modelo = novo_modelo
        else:
           print('Erro. Tem que ser uma string.')


    def set_ano(self, novo_ano:int):
        if type(novo_ano) == int:
           self.ano = novo_ano
        else:
            print('Erro: Valor inconsistente.')

    def set_valor(self, novo_valor):
        if novo_valor >= 0:
            self.valor = novo_valor
        else:
            print('Erro: Valor inconsistente.')

    def mostrar_dados(self):
         print('Mostrar dados:',self.ano)
         print('Modelo:',self.modelo)
         print('Valor:',self.valor)


    def aumentar_valor(self, aumento: float):
         if aumento > 0:
            self.valor += aumento
         else:
             print("Aumento deve ser positivo.")

