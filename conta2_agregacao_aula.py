"""             Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
Atalhos: ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Este exercício não usa herança e nem classe abstrata (ABC).

- Vamos implementar a classe conta corrente.

- Primeira ideia dos atributos (características) da classe conta corrente:
número da conta;
nome do titular;
sobrenome do titular;
cpf do titular;
saldo da conta; e
vl_limite da conta.

Obs.: o valor limite é um valor que o banco disponibiliza e o titular pode usar.

- Ideia de agregação:
. Temos muitos atributos e estes atributos não são naturais de uma conta corrente:
nome do titular;
sobrenome do titular;
cpf do titular;
. Pois, esses atributos são do titular e não da conta corrente.
. Assim, crie uma nova classe (classe Titular) e faça uma agregação,
  ou seja, agrege um objeto da classe Titular a uma conta corrente.
. Portanto, a classe Conta tem como atributo um objeto da classe Titular.
. Os atributos de Conta também podem ser referência (objeto) para outra classe

- Vamos usar agregação na implementação:
1. Crie a classe Titular com os atributos:
nome do titular;
sobrenome do titular;
cpf do titular.
2. Crie a classe Conta com os atributos:
número da conta;
obj_titular;  # Um objeto da outra classe (classe Titular)
saldo; e
vl_limite.

- Resumo:
Um atributo de uma classe pode ser um objeto de outra classe.
- Exemplo:
O atributo obj_titular da classe Conta é um objeto da classe Titular.

- Valor default na classe Conta:
Na declaração dos parâmetros no construtor da classe Conta, atribua um
valor default (padrão) de 1000.00 reais para o parâmetro valor limite.

- Como implementar o construtor das duas classes:
class Titular(object):            # class Titular:
    def __init__(self, cpf, nome, sobrenome=""):  # Construtor com valor default
        self.cpf = cpf
        self.nome = nome          # Atributos de instância
        self.sobrenome = sobrenome

class Conta(object):                    # class Conta:
    def __init__(self, numero, o_titular, saldo, limite=1000.0):  # Com valor default
        self.numero = numero
        self.titular = o_titular
        # O atributo self.titular recebe o endereço do objeto da classe Titular
        self.saldo = saldo
        self.limite = limite

- Implemente:
1- Crie a classe Titular com os atributos cpf, nome, sobrenome
2- Crie (instancie) um objeto da classe Titular, teste
3- Crie alguns métodos gets e sets, teste
4- Crie o método funcional que retora o nome completo do titular, teste
5- Crie a classe Conta com os atributos numero, obj_titular, saldo, limite.
6- Crie um objeto da classe Conta usando o objeto da classe Titular criado
7- Crie alguns métodos gets e sets, teste
8- No main, mostre o endereço hexadecimal do objeto titular criado
9- No main, mostre o endereço hexadecimal do objeto conta criado
10- No main, mostre o nome, sobrenome e cpf usando o objeto da classe Titular
11- Altere o nome do objeto titular, teste.
12a- No main, mostre o nome, sobrenome e cpf usando o objeto da classe Conta.
12b- Na classe Conta, crie o método para consultar o nome do titular, teste
12c- Na classe Conta, crie o método para consultar o sobrenome do titular, teste
12d- Na classe Conta, crie o método para consultar o cpf do titular, teste
13- Altere o nome do objeto titular usando o objeto da classe Conta, teste.
14- Crie o método extrato reduzido para mostrar os seguintes dados:
    número da conta e saldo da conta
15- Crie o método extrato normal para mostrar os seguintes dados:
    nome, sobrenome, cpf, número da conta e saldo da conta
16- Na classe Conta, crie o método parar mostrar todos os dados do atributo
    titular da classe Conta.
17- Faça um depósito, teste.
18- Faça um saque, teste.
19- Refaça o método anterior com uma RN (regra de negócio) do banco,
    ou seja, com crítica.
20- Cadastre mais uma conta corrente, teste
21- Faça uma transferência, teste.

"""


class Titular(object):            # class Titular:
    def __init__(self, cpf, nome, sobrenome=""):  # Construtor com valor default
        self.cpf = cpf
        self.nome = nome          # Atributos de instância
        self.sobrenome = sobrenome
    def get_cpf(self):            # Métodos gets e sets
        return self.cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_sobrenome(self):
        return self.sobrenome
    def nome_completo(self):                        # Método funcional
        nome_c = self.nome + " " + self.sobrenome   # Usa concatenação de strings
        # nome_c = f'{self.nome} {self.sobrenome}'  # Usa o f-string
        # As duas linhas acima são equivalentes
        return nome_c


class Conta(object):                    # class Conta:
    def __init__(self, numero, o_titular, saldo, limite=1000.0):
        self.numero = numero
        self.titular = o_titular
        # O atributo self.titular recebe o endereço do objeto da classe Titular
        self.saldo = saldo
        self.limite = limite
    def get_saldo(self):
        return self.saldo
    def get_titular(self):                  # Retorna o endereço do objeto titular
        return self.titular
    # Chama os métodos da classe Titular dentro destes métodos da classe Conta
    def get_titular_nome(self):             # Retorna nome do titular
        return self.titular.get_nome()
    def set_titular_nome(self, novo_nome):  # Altera nome do titular
        self.titular.set_nome(novo_nome)    # self.titular.nome = novo_nome
    def get_titular_sobrenome(self):        # Retorna sobrenome do titular
        return self.titular.get_sobrenome()
    def get_titular_cpf(self):              # Retorna cpf do titular
        return self.titular.get_cpf()
    def extrato_reduzido(self):
        print(f"Extrato 1:\nNúmero: {self.numero}, Saldo: {self.saldo}")
    def extrato_normal(self):                # Usando métodps da classe Titular
        print(f'Extrato 2:\nNome: {self.titular.get_nome()} '
        f'{self.titular.get_sobrenome()} CPF: {self.titular.get_cpf()}')
        print(f"\nNúmero: {self.numero}, Saldo: {self.saldo}")
    def dados_titular(self):
        # return self.titular.__dict__
        return vars(self.titular)
    def deposito(self, valor):
        self.saldo += valor
    # def saque(self, valor):             # Sem crítica
    #     self.saldo -= valor
    def saque(self, valor):             # Com crítica (RN - Regra de Negócio)
        if self.saldo + self.limite < valor:
            print('Saldo insuficiente.')
            return False
        else:
            self.saldo -= valor
            print('Saque realizado.')
            return True
