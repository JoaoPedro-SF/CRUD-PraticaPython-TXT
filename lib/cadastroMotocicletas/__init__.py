from time import sleep
def cadastrarMotocicletas():
    sleep(1.5)
    while True:
        opcao = input(f'''
{'-' * 60}
{'Menu Motocicletas'.center(60)}
                              + {contarMotocicletas()} MOTO(S) CADASTRADO(S)
                              + 
                              + ÚLTIMO CADASTRO
                              + {ultimaMotocicletaCadastrada().rstrip()}
[1]Cadastrar Motocicletas     + 
[2]Listar Motocicletas        + 
[3]Deletar Motocicleta        + 
[4]Buscar pelo modelo         + 
[5]Atualizar Motocicleta      +
[6]Sair                       + 
------------------------------------------------------------

Escolha uma opção acima: ''')
        sleep(1)
        if opcao == '1':
            cadastrarMotocicleta()
        elif opcao == '2':
            listarMotocicletas()
        elif opcao == '3':
            deletarMotocicleta()
        elif opcao == '4':
            buscarMotocicletasModelo()
        elif opcao == '5':
            atualizarMotocicleta()
        elif opcao == '6':
            break
        else:
            print('ERRO! Digite uma opcão válida!')

def contarMotocicletas():
    with (open('crudMotocicletas.txt', 'r')) as motocicletas:
        return  len(motocicletas.readlines())

def atualizarMotocicleta():
    motocicleta = open('crudMotocicletas.txt', 'r')
    aux = []
    for i in motocicleta:
        aux.append(i)
    nomeDeletado = int(input('Digite o indice para ser Atualizado: '))
    motocicleta.close()
    nomeDeletado -= 1
    cont = 0
    try:
        aux.pop(nomeDeletado)
        cont += 1
    except:
        print('Esse indice não existe, entre na lista de Motocicletas!')
    motocicleta = open('crudMotocicletas.txt', 'w')
    for i in aux:
        motocicleta.write(i)
    if cont == 1:
        idMotocicleta = input('Escolha o id da motocicleta: ')
        modelo = input('Escreva o modelo da motocicleta: ')
        cor = input('Escreva a cor da motocicleta: ')
        preco = input('Escreva o Preço da motocicleta: ')
        try:
            motocicleta = open('crudMotocicletas.txt', 'a')
            dados = f'idMotocicleta: {idMotocicleta}; Modelo: {modelo}; Cor: {cor}; Preço: {preco}; \n'
            motocicleta.write(dados)
            motocicleta.close()
            print(f'Motocicleta cadastrada com sucesso!')
        except:
            print('Erro ao cadastrar essa Motocicleta!')
    else:
        sleep(1)
def cadastrarMotocicleta():
    idMotocicleta = input('Escolha o id da motocicleta: ')
    modelo = input('Escreva o modelo da motocicleta: ')
    cor = input('Escreva a cor da motocicleta: ')
    preco = input('Escreva o Preço da motocicleta: ')
    try:
        motocicleta = open('crudMotocicletas.txt', 'a')
        dados = f'idMotocicleta: {idMotocicleta}; Modelo: {modelo}; Cor: {cor}; Preço: {preco}; \n'
        motocicleta.write(dados)
        motocicleta.close()
        print(f'Motocicleta cadastrada com sucesso!')
    except:
        print('Erro ao cadastrar essa Motocicleta!')

def listarMotocicletas():
    motocicleta = (open('crudMotocicletas.txt', 'r'))
    cont = 0
    for i in motocicleta:
        cont += 1
        print(f'Indice: {cont}; {i.split(";")[0]};{i.split(";")[1]};{i.split(";")[2]};{i.split(";")[3].rstrip()};')
    motocicleta.close()
    sleep(1)

def deletarMotocicleta():
    motocicletas = open('crudMotocicletas.txt', 'r')
    aux = []
    for i in motocicletas:
        aux.append(i)
    nomeDeletado = int(input('Digite o indice para ser deletado: '))
    motocicletas.close()
    nomeDeletado -= 1
    try:
        aux.pop(nomeDeletado)
        print(f'Motocicleta deletada com sucesso!')
    except:
        print('Esse indice não existe, entre na lista de Motocicletas!')
    motocicletas = open('crudMotocicletas.txt', 'w')
    for i in aux:
        motocicletas.write(i)
    listarMotocicletas()

def buscarMotocicletasModelo():
    modelo = input('Digite o modelo a ser procurado: ').upper()
    motocicletas = open('crudMotocicletas.txt', 'r')
    cont = 0
    for motocicleta in motocicletas:
        if modelo in motocicleta.split(";")[1].upper():
            print(motocicleta)
            cont += 1
    if cont == 0:
        print('Motocicleta não encontrado!')
    motocicletas.close()
    sleep(1)
def ultimaMotocicletaCadastrada():
    try:
        with (open('crudMotocicletas.txt', 'r')) as motocicleta:
            ultimaMotocicleta = motocicleta.readlines()[-1]

            return ultimaMotocicleta
    except:
        return 'nenhum'