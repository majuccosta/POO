# Sintaxe: from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2
from cliente_aula import Cliente, Endereco
if __name__ == '__main__':
    cliente1 = Cliente('Luis', 2005)  # Chama construtor de Cliente
    print('- Nome:', cliente1.get_nome())
    print('Ano Nascimento:', cliente1.get_ano_nascimento())
    print('Idade:', cliente1.calcula_idade(), "anos.")
    print(f'Idade: {cliente1.calcula_idade()} anos.')  # f-string
    cliente1.insere_endereco('Belo Horizonte', 'MG')  # Chama método, passa 2 strings
    cliente1.mostra_enderecos()
    cliente2 = Cliente('Maria', 2007)
    cliente2.insere_endereco('Salvador', 'BA')
    cliente2.insere_endereco('Rio de Janeiro', 'RJ')
    print('- Nome:', cliente2.get_nome())
    cliente2.mostra_enderecos()
    endereco = Endereco('Brasília', 'DF')  # Chama construtor da classe Endereco
    cliente2.insere_endereco2(endereco)    # Chama o método, passa um objeto de Endereco
    print('- Nome:', cliente2.get_nome())
    cliente2.mostra_enderecos()
    cliente2.mostra_enderecos2()           # Equivalente as duas linhas anteriores
    # Cria o cliente 3
    cliente3 = Cliente('João', 2006)
    cliente3.insere_endereco('São Paulo', 'SP')
    print('- Nome:', cliente3.get_nome())
    cliente3.mostra_enderecos()
    cliente3.mostra_enderecos2()           # Equivalente as duas linhas anteriores
    cliente2.mostra_enderecos3()
    cliente2.remove_endereco_objeto(endereco)
    cliente2.mostra_enderecos3()

