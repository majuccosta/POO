# Sintaxe:
# from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2, NomeClasse3
from carrinho_compra_aula import CarrinhoCompra, Produto, Cliente
if __name__ == '__main__':
    cliente1 = Cliente("224", 'Ailton')  # Chama o contrutor da classe Cliente
    print(cliente1)
    cliente2 = Cliente("123")            # Chama o contrutor da classe Cliente
    print(cliente2)
    carrinho1 = CarrinhoCompra("12", cliente1)  # (num_pedido, objeto_Cliente)
    print('Carrinho compra: Número:', carrinho1.get_num_pedido())
    print('\tNome:', carrinho1.get_cliente_nome())
    p1_arroz = Produto("1", 'Arroz', 30.0)  # Chama o construtor da classe Produto
    print(p1_arroz)
    p2_feijao = Produto("2", 'Feijão', 9.00, 3)  # Com quantidade
    print(p2_feijao)
    carrinho1.mostra_carrinho()           # O carrinho está vazio
    carrinho1.insere_produto(p1_arroz)    # Chama o método, passa objeto Produto
    carrinho1.mostra_carrinho()
    carrinho1.insere_produto(p2_feijao)
    carrinho1.mostra_carrinho()
    carrinho1.mostra_carrinho2()           # Com quantidade
    carrinho1.calcula_total()
    carrinho1.insere_produto(p2_feijao)
    carrinho1.remove_produto(p2_feijao)   # Teste sem erro
    carrinho1.insere_produto(p2_feijao)
    carrinho1.remove_produto2(p2_feijao)    # Teste sem erro
    carrinho1.remove_produto2(cliente2)     # Teste com erro
    # ValueError: list.remove(x): x not in list
    carrinho1.mostra_carrinho2()
    p3_farinha = Produto("3", 'Farinha', 5.00, 2)
    carrinho1.insere_produto(p3_farinha)
    carrinho1.mostra_carrinho2()
    carrinho1.fecha_carrinho()

    carrinho1.calcula_total()
