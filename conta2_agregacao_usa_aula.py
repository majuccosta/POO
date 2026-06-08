# from conta_agregacao import *
# Sintaxe: from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2
from conta2_agregacao_aula import Conta, Titular
if __name__ == '__main__':          # Atalho: mai <tab>
    titular1 = Titular('371-1', 'Lia', 'Oliveira')  # Objeto da classe Titular
    print('Nome:', titular1.get_nome())
    print('Nome completo:', titular1.nome_completo())
    # Cria objeto da classe Conta usando o objeto da classe Titular
    conta1 = Conta('123-4', titular1, 1200.00, 2000.00)
    print(titular1)  # <conta_agregacao.Titular object at 0x000002B9DBA4AFD0>
    print(conta1)    # <conta_agregacao.Conta object at 0x000002B9DBA4AF70>
    print(conta1.get_titular())
    # <conta_agregacao.Titular object at 0x000002B9DBA4AFD0>, endereço do atributo
    print('Nome:', titular1.get_nome())  # Consulta usando a classe Titular
    print('Sobrenome:', titular1.get_sobrenome())
    print('CPF:', titular1.get_cpf())
    titular1.set_nome('Ana')            # Altera o nome usando a classe Titular
    print('Nome:', titular1.get_nome())
    print('Nome completo:', titular1.nome_completo())
    print('Nome:', conta1.get_titular().get_nome())  # Consulta usando a classe Conta
    print('Nome:', conta1.get_titular_nome())  # Consulta usando a classe Conta
    print('Sobrenome:', conta1.get_titular_sobrenome())
    print('CPF:', conta1.get_titular_cpf())
    conta1.set_titular_nome('Alice')        # Altera o nome usando a classe Conta
    print('Nome:', conta1.get_titular_nome())
    conta1.extrato_reduzido()
    conta1.extrato_normal()
    print('conta1.dados_titular():', conta1.dados_titular())
    print(conta1.get_titular())         # Retorna o endereço
    conta1_titular = conta1.get_titular()
    print(conta1_titular.__dict__)
    print(vars(conta1_titular))
    print("----------------")
    print(titular1.__dict__)            # Métodos semelhantes
    print(vars(titular1))
    print("----------------")
    conta1.deposito(200)
    conta1.saque(100)
    titular2 = Titular('388-1', 'Paulo', 'Pereira')  # Objeto da classe Titular
    print('Nome:', titular2.get_nome())
    print('Nome completo:', titular2.nome_completo())
    conta2 = Conta('143-6', titular2, 900.00)

    print('- special method or dunder:')
    print(titular1.__class__)           # <class 'conta_agregacao.Titular'>
    print(titular1.__class__.__name__)  # Titular

