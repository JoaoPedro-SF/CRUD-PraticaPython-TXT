from time import sleep

def cadastrarClientes():
    sleep(1.5)
    while True:
        opcao = input(f'''
{'-' * 60}
{'Menu Clientes'.center(60)}
                              + {contarClientes()} CLIENTE(S) CADASTRADO(S)
                              + 
                              + ÚLTIMO CADASTRO
                              + {ultimoClienteCadastrado().rstrip()}
[1]Cadastrar Cliente          + 
[2]Listar Clientes            + 
[3]Deletar Cliente            + 
[4]Buscar Cliente pelo nome   + 
[5]Atualizar Cliente          +
[6]Sair                       + 
------------------------------------------------------------

Escolha uma opção acima: ''')
        sleep(1)
        if opcao == '1':
            cadastrarCliente()
        elif opcao == '2':
            listarCliente()
        elif opcao == '3':
            deletarCliente()
        elif opcao == '4':
            buscarClienteNome()
        elif opcao == '5':
            atualizarCliente()
        elif opcao == '6':
            break
        else:
            print('ERRO! Digite uma opcão válida!')

def contarClientes():
    with (open('crudClientes.txt', 'r')) as clientes:
        return  len(clientes.readlines())

def atualizarCliente():
    cliente = open('crudClientes.txt', 'r')
    aux = []
    for i in cliente:
        aux.append(i)
    nomeDeletado = int(input('Digite o indice para ser Atualizado: '))
    cliente.close()
    nomeDeletado -= 1
    cont = 0
    try:
        aux.pop(nomeDeletado)
        cont += 1
    except:
        print('Esse indice não existe, entre na lista de clientes!')
    cliente = open('crudClientes.txt', 'w')
    for i in aux:
        cliente.write(i)
    if cont == 1:
        idCliente = input('Escolha o id do Cliente: ')
        nome = input('Escreva o nome do cliente: ')
        telefone = input('Escreva o telefone do Cliente: ')
        cpf = input('Escreva o CPF do Cliente: ')
        try:
            cliente = open('crudClientes.txt', 'a')
            dados = f'idCliente: {idCliente}; Nome: {nome}; Telefone: {telefone}; CPF: {cpf}; \n'
            cliente.write(dados)
            print(f'Cliente cadastrado com sucesso!')
        except:
            print('Erro ao cadastrar esse cliente!')
        cliente.close()
    else:
        sleep(1)
def cadastrarCliente():
    idCliente = input('Escolha o id do Cliente: ')
    nome = input('Escreva o nome do cliente: ')
    telefone = input('Escreva o telefone do Cliente: ')
    cpf = input('Escreva o CPF do Cliente: ')
    try:
        cliente = open('crudClientes.txt', 'a')
        dados = f'idCliente: {idCliente}; Nome: {nome}; Telefone: {telefone}; CPF: {cpf}; \n'
        cliente.write(dados)
        cliente.close()
        print(f'Cliente cadastrado com sucesso!')
    except:
        print('Erro ao cadastrar esse cliente!')

def listarCliente():
    clientes = (open('crudClientes.txt', 'r'))
    cont = 0
    for i in clientes:
        cont += 1
        print(f'Indice: {cont}; {i.split(";")[0]};{i.split(";")[1]};{i.split(";")[2]};{i.split(";")[3].rstrip()};')
    clientes.close()
    sleep(1)

def deletarCliente():
    clientes = open('crudClientes.txt', 'r')
    aux = []
    for i in clientes:
        aux.append(i)
    nomeDeletado = int(input('Digite o indice para ser deletado: '))
    clientes.close()
    nomeDeletado -= 1
    try:
        aux.pop(nomeDeletado)
        print(f'Cliente deletado com sucesso!')
    except:
        print('Esse indice não existe, entre na lista de clientes!')
    clientes = open('crudClientes.txt', 'w')
    for i in aux:
        clientes.write(i)
    listarCliente()

def buscarClienteNome():
    nome = input('Digite o nome a ser procurado: ').upper()
    clientes = open('crudClientes.txt', 'r')
    cont = 0
    for cliente in clientes:
        if nome in cliente.split(";")[1].upper():
            print(cliente)
            cont += 1
    if cont == 0:
        print('Cliente não encontrado!')
    clientes.close()

def ultimoClienteCadastrado():
    try:
        with (open('crudClientes.txt', 'r')) as cliente:
            ultimoCliente = cliente.readlines()[-1]

            return ultimoCliente
    except:
        return 'nenhum'
