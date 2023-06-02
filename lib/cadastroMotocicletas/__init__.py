from time import sleep
def cadastrarMotocicletas():
    sleep(1.5)
    while True:
        opcao = input(f'''
{'-' * 60}
{'Menu Motocicletas'.center(60)}
                              + {'teste'} MOTO(S) CADASTRADO(S)
                              + 
                              + ÚLTIMO CADASTRO
                              + {'teste'}
[1]Cadastrar Motocicletas     + 
[2]Listar Motocicletas        + 
[3]Deletar Motocicleta        + 
[4]Buscar Moto pelo nome      + 
[5]Atualizar Motocicleta      +
[6]Sair                       + 
------------------------------------------------------------

Escolha uma opção acima: ''')
        sleep(1)
        if opcao == '1':
            break
            cadastrarCliente()

        elif opcao == '2':
            break
            listarCliente()
        elif opcao == '3':
            break
            deletarCliente()
        elif opcao == '4':
            break
            buscarClienteNome()
        elif opcao == '5':
            break
            atualizarCliente()
        elif opcao == '6':
            break
        else:
            print('ERRO! Digite uma opcão válida!')