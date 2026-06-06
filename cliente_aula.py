""" Com base nos conceitos de Programação Orientada a Objetos (POO) e
associação de classes, implemente as classes necessárias para realizar
a manutenção de um cliente.

- Vamos usar as seguintes características (atributos) de cliente:
nome,
ano_nascimento, e
seus endereços, ou seja, cada cliente pode ter mais de um endereço.

- Usamos apenas as seguintes características (atributos) de endereço:
cidade,
estado.

- Como implementar o construtor das duas classes:
class Cliente:   # Nome de classe no singular, pois é um modelo
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.enderecos = []  # Nome de lista no plural, pode ter vários conteúdos
        # O atributo self.endereco recebe um objeto da classe Endereco

class Endereco:
    def __init__(self, cidade, estado='DF'):
        self.cidade = cidade
        self.estado = estado

- Implemente:

1- A classe Cliente
2- O construtor com os atributos nome, ano_nascimento e endereços
    Como implementar o atributo endereços?
3- Os métodos gets e sets de nome e ano_nascimento, teste
4- Um objeto da classe Cliente apenas com o nome e ano de nascimento, teste
5- o método calcula idade, não recebe parãmetros e retorna a idade, teste
6- A classe Endereco
7- O construtor com os atributos cidade e estado com pelo menos um valor default
8a- Crie os métodos gets e sets, teste
8b- O método str para retornar o padrão: Nome da cidade - Sigla do estado
9- Insira um endereço para um cliente. Na classe Cliente, crie o método
   insere_endereco, ele recebe duas strings como parâmetros, cria um objeto
   da classe Endereco e armazena-o na lista. Teste
10- Na classe Cliente, crie o método mostra_enderecos, teste
11- Crie mais um cliente e insira dois endereços pra ele, teste
12- Crie pelo menos dois objetos da classe Endereço
13- Em Cliente, crie o método insere_endereco2, ele recebe um objeto
   da classe Endereco e armazena-o na lista, teste
14- Crie o método mostra_enderecos2 com o objetivo de melhorar
    o layout do método, antes de mostrar todos os endereços, ele deve
    mostrar também o nome do cliente, teste.
15- Chame o método mostra_enderecos2 antes de inserir os endereços,
    no início do método main. Se não tiver endereço cadastrado, o método
    deve mostrar msg "Cliente não tem endereço cadastrado", teste
16- Crie um método para remover um endereço de um cliente usando um objeto, teste
17- Crie o método revome_endereco_cidade para remover um endereço de um cliente,
    o usuário fornece o nome da cidade do endereço que será removido, teste

"""


from datetime import datetime
# class Cliente(object):  # Três formas de criar uma classe
# class Cliente():
class Cliente:   # Nome de classe no singular, pois é um modelo
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.enderecos = []  # Nome de lista no plural, pode ter vários conteúdos
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_ano_nascimento(self):
        return self.ano_nascimento
    def set_ano_nascimento(self, novo_ano):
        self.ano_nascimento = novo_ano
    # def calcula_idade(self):      # Uso o valor do ano estático
    #     ano_atual = 2025
    #     return ano_atual - self.ano_nascimento
    def calcula_idade(self):        # Pega o ano do sistema operacional
        ano_atual = datetime.now().year
        return ano_atual - self.ano_nascimento
    # Insere endereço com strings (cidade e estado)
    def insere_endereco(self, cidade, estado='DF'):  # Recebe duas strings
        o_endereco = Endereco(cidade, estado)  # Chama o construtor da classe Endereco
        self.enderecos.append(o_endereco)      # Armazena na lista
        # self.enderecos.append(Endereco(cidade, estado))
        # Equivalente as 2 anteriores
    # Mostra endereços simples
    def mostra_enderecos(self):
        print(f'- Endereços do cliente:')
        for o_endereco in self.enderecos:    # Percorre a lista self.enderecos
            # print(o_endereco.get_cidade(), "-", o_endereco.get_estado())  # Não usa o str
            print(o_endereco)                # Usa o método str
    # Insere endereço passando um objeto Endereco
    def insere_endereco2(self, o_endereco):  # Recebe um objeto da classe Endereco
        self.enderecos.append(o_endereco)    # Armazena na lista
    # def insere_endereco2(self, endereco_obj):  # Com crítica
    #     if isinstance(endereco_obj, Endereco):
    #         self.enderecos.append(endereco_obj)
    #     else:
    #         print("Erro: O argumento deve ser um objeto da classe Endereco.")
    def mostra_enderecos2(self):
        print(f'- Endereços do cliente {self.nome}:')
        for o_endereco in self.enderecos:
            print(o_endereco.get_cidade(), "-", o_endereco.get_estado())
            # print(f" - {o_endereco}")
    # Mostra endereços com melhor formatação
    def mostra_enderecos3(self):
        # if len(self.enderecos) == 0: # if self.enderecos == []:  # lista vazia?
        if not self.enderecos:  # lista vazia?
            print("Cliente não tem endereço cadastrado.")
        else:
            print(f'- Endereços do cliente {self.nome}')
            for o_endereco in self.enderecos:
                print(o_endereco.get_cidade(), o_endereco.get_estado())
                # print(f" - {o_endereco}")
    # Remove endereço passando um objeto
    def remove_endereco_objeto(self, o_endereco):
        self.enderecos.remove(o_endereco)
    # def remove_endereco(self, endereco_obj):
    #     if endereco_obj in self.enderecos:
    #         self.enderecos.remove(endereco_obj)
    #         print("Endereço removido com sucesso.")
    #     else:
    #         print("Erro: Endereço não encontrado.")
    # Remove endereço pela cidade


# Três formas de criar uma classe
# class Endereco(object):
# class Endereco():
class Endereco:  # Nome de classe no singular, pois é um modelo
    def __init__(self, cidade, estado='DF'):
        self.cidade = cidade
        self.estado = estado
    def get_cidade(self):
        return self.cidade
    def set_cidade(self, nova_cidade):
        self.cidade = nova_cidade
    def get_estado(self):
        return self.estado
    def set_estado(self, novo_estado):
        self.estado = novo_estado
    def __str__(self):
        return f"{self.cidade} - {self.estado}"