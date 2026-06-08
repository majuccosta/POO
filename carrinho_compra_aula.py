class Cliente(object):                 # class Cliente:
    def __init__(self, cpf, nome=""):  # Construtor com valor default
        self.cpf = cpf
        self.nome = nome
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, cpf):
        self.cpf = cpf
    def get_nome(self):                 # Consulta
        return self.nome
    def set_nome(self, nome):           # Altera
        self.nome = nome
    def __str__(self):
        dados = f'- Cliente:\nCPF: {self.cpf}, Nome: {self.nome}'
        return dados


class CarrinhoCompra(object):       # class CarrinhoCompra:
    def __init__(self, num_pedido, o_cliente):
        self.num_pedido = num_pedido
        self.o_cliente = o_cliente  # Um objeto da classe Cliente
        self.l_produtos = list()    # self.l_produtos = []
        # Colocar na lista l_produtos, objetos da classe Produto
    def get_num_pedido(self):
        return self.num_pedido
    def get_cliente_nome(self):     # Nome cliente
        return self.o_cliente.get_nome()  # Usa um método de outra classe
    def insere_produto(self, o_produto):  # Insere produto no carrinho
        self.l_produtos.append(o_produto)
    def mostra_carrinho(self):            # Mostra produtos no carrinho
        qtd = len(self.l_produtos)
        if qtd == 0:  # if self.l_produtos == []:  # if not self.l_produtos:
            print('Carrinho vazio.')
        else:
            print('- Mostra carrinho 1:')
            for o_produto in self.l_produtos:
                print('Descrição:', o_produto.get_nome())
    def mostra_carrinho2(self):           # Mostra produtos no carrinho
        qtd = len(self.l_produtos)
        if qtd == 0:  # if self.l_produtos == []:  # if not self.l_produtos:
            print('Carrinho vazio.')
        else:
            print('- Mostra carrinho 2:')
            for o_produto in self.l_produtos:  # Solução 1
                print(o_produto)               # print(o_produto.__str__())
            # for i, o_produto in enumerate(self.l_produtos):  # Solução 2
            #     print(i, ' - ', o_produto)   # print(o_produto.__str__())
            print('Quantidade de itens:', qtd)
    def calcula_total(self):                   # Calcula valor total da compra
        qtd = len(self.l_produtos)
        if qtd == 0:  # if self.l_produtos == []:  # if not self.l_produtos:
            print('Carrinho vazio.')
        else:
            total = 0                              # Somador
            for o_produto in self.l_produtos:  # Lista com os produtos no carrinho
                total += o_produto.get_preco() * o_produto.get_qtd()
            print(f'Valor total: R$ {total:.2f}')
    def remove_produto(self, o_produto):           # Sem crítica
        self.l_produtos.remove(o_produto)
    def remove_produto2(self, o_produto):          # Com crítica
        if o_produto in self.l_produtos:           # Operador in
            self.l_produtos.remove(o_produto)
            print('Produto removido.')
        else:
            print('Produto não está no carrinho.')

    def fecha_carrinho(self):  # Falta verificar se o carrinho está vazio
        print('- Finalizando a compra 1:')
        self.mostra_carrinho2()
        self.calcula_total()


class Produto(object):                                # class Produto:
    def __init__(self, idt, nome, preco=0.0, qtd=1):  # Construtor com default
        self.idt = idt                                # Atributos
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_preco(self):
        return self.preco
    def set_preco(self, novo_preco):
        self.preco = novo_preco
    def get_qtd(self):
        return self.qtd
    def set_qtd(self, nova_qtd):
        self.qtd = nova_qtd
    def __str__(self):                                  # Sobrescreve o método str
        dados = f'Produto: Idt: {self.idt}, nome: {self.nome}, ' \
                f'preço: {self.preco}, qtd.: {self.qtd}'
        return dados