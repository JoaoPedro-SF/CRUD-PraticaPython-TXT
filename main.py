from time import sleep
from lib.cadastroClientes import *
from lib.cadastroMotocicletas import *

def menu():
    voltarMenuPrincipal = 'S'
    while voltarMenuPrincipal == 'S':
        opcao = input(f'''
============================================================
{'Projeto CRUD Concessionária V1.1'.center(60)}
============================================================
 {'MENU PRINCIPAL'.center(60)}
[1] - Menu Clientes           +
[2] - Menu Motocicletas       + 
[3] - Sair                    +  
============================================================

Escolha uma opção acima: ''')
        if opcao == '1':
            cadastrarClientes()
        elif opcao == '2':
            cadastrarMotocicletas()
        elif opcao == '3':
            print('Saindo do sistema... Até logo!')
            break
        else:
            print('ERRO! Digite uma opcão válida!')

if __name__ == '__main__':
    menu()
