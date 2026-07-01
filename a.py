class Iphone(object):
     def __init__(self, modelo, ano, valor):
         self.modelo = modelo
         self.ano = ano
         self.valor = valor
     def get_modelo(self):
         return self.modelo
     def get_ano(self):
         return self.ano
     def get_valor(self):
         return self.valor
     def set_modelo(self,novo_modelo):
         self.modelo= novo_modelo
     def set_ano(self, novo_ano):
         self.ano = novo_ano
     def set_valor(self, novo_valor):
         if novo_valor >= 0:
             self.valor = novo_valor
         else:
          print('Erro: Valor inconsistente.')

     def mostrar_dados(self):
         print('Mostrar dados:',self.ano)
         print('Modelo:',self.modelo)
         print('Valor:',self.valor)

if __name__== '__main__':
    celular1=Iphone(13,2023,3500)
    print(celular1)
    celular2= Iphone(11,2020,2000)
    print(celular2)
    print('Iphone 1\nModelo:',celular1.get_modelo())
    print('Ano:',celular1.get_ano())
    print('Valor:',celular1.get_valor())
    print('Iphone 2\nModelo:',celular2.get_modelo())
    print('Ano:',celular2.get_ano())
    print('Valor:',celular2.get_valor())
    celular1.set_valor(-12000)
    print('Valor atualizado do celular 1:',celular1.get_valor())
    celular2.set_modelo(14)
    print('Valor atualizado do celular 2:',celular2.get_modelo())