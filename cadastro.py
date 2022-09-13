import menu
import time
import os

catalogo = {}
produto = ''
valor = ''

print_cad ='''
    |--------------------------------------------------------------------------------------------------|
    |                                    Digite o nome do produto:                                     |
    |                                    Ou Digite 'X' para sair.                                      |
    |--------------------------------------------------------------------------------------------------|'''

print_val =f'''
    |--------------------------------------------------------------------------------------------------|
    |                                    Digite o valor do produto ?                                   |
    |                                    Subistitia ' , ' por ' . ' ponto                              | 
    |                                    Ou Digite 'X' para sair.                                      |
    |--------------------------------------------------------------------------------------------------|'''

print_menu =f'''
    |--------------------------------------------------------------------------------------------------|
    |                                    Opções.                                                       |
    |                                    1- Cadastrar um Produto                                       | 
    |                                    2- Ver catalogo de produto                                    |
    |                                    3- Deletar produto                                            |
    |                                    4- Voltar ao menu anterior                                    |
    |--------------------------------------------------------------------------------------------------|'''

print_prod ='''
    |--------------------------------------------------------------------------------------------------|
    |                                      Produtos cadastrados                                        |
    |--------------------------------------------------------------------------------------------------|
    |         Produtos                                                     Preço                       |
    |                                                                                                  |'''

print_fim =  """
    |--------------------------------------------------------------------------------------------------|
"""




def cadastro():
    os.system('cls')
    global catalogo
    global produto
    global valor

    #while produto != 'x':
    produto = ''
    valor = 0
    print(print_cad)
    produto= input('\tNome do Produto: ')

    if produto.isalpha() == False and len(produto) < 2 :
        print('Entrada Inválida')
        time.sleep(3)
        cadastro()

    else:
        os.system('cls')
        while type(valor) != float:
            print(print_val)
            valor = input(f'Qual o valor de {produto}: ')
            if valor.lower() == 'x':
                print('Voltando ao menu principal')
                time.sleep(3)
                cadastro()
                
            elif valor.replace(".", "", 1).isdigit() == False:
                print('Entrada Inválida')

            else:
                valor = round(float(valor),2)
                catalogo[(produto.lower()).capitalize()] = valor
    
    cad_menu()


def cad_menu():
    
    os.system('cls')
    print(print_menu)
    opcao_cadastro = input('Digite a opção: ')
    print(opcao_cadastro)
    if str(opcao_cadastro) == '1':
        cadastro()

    elif str(opcao_cadastro) == '2':
        catalogo_prod()

    elif str(opcao_cadastro) == '3':
        #enviar_catalogo()
        menu.menu_funcs(catalogo)

    else:
        print('Entrada Inválida.\n Digite uma opção valida')
        cad_menu()
        

def catalogo_prod():
    global catalogo
    os.system('cls')
    print(print_prod, end='')
    for i in  catalogo.keys():
        print(f"""
    |         {i:<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(catalogo[i]):<6s}                  |""", end=''
        )
    print(print_fim)
    print("\nPara sair aperte 'X'")
    op = input('Aperte a Tecla:').lower()
    if op == 'x':
        cad_menu()
    else:
        print('Tecla invalida!!!')
        time.sleep(3)
        catalogo_prod()

def deletar_item_catalago():
    global catalogo
    print('|-------------------------------------------------------------------------------|')
    apagar = str(input('Qual catalago gostaria de deletar: '))
    catalogo.pop(deletar_item_catalago, None)

def deletar_item_catalago():
    global catalogo
    print('|-------------------------------------------------------------------------------|')
    apagar = str(input('Qual catalago gostaria de deletar: '))
    catalogo.pop(deletar_item_catalago, None)
    
def enviar_catalogo():
    global catalogo
    catalogo = catalogo
    return catalogo
