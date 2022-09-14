import menu
import time
import os

catalogo = {}
produto = ''
valor = ''

print_cad ='''
    |--------------------------------------------------------------------------------------------------|
    |                                    Digite o nome do produto:                                     |
    |                                    Ou Digite 'S' para sair.                                      |
    |--------------------------------------------------------------------------------------------------|'''

print_val =f'''
    |--------------------------------------------------------------------------------------------------|
    |                                    Digite o valor do produto ?                                   |
    |                                    Subistitia ' , ' por ' . ' ponto                              | 
    |                                    Ou Digite 'S para sair.                                      |
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
        print('\tEntrada Inválida')
        time.sleep(3)
        cadastro()

    else:
        os.system('cls')
        while type(valor) != float:
            print(print_val)
            valor = input(f'\tQual o valor de {produto}: ')
            if valor.upper() == 'S':
                print('\tVoltando ao menu principal')
                time.sleep(3)
                cad_menu()
                
            elif valor.replace(".", "", 1).isdigit() == False:
                print('\tEntrada Inválida')

            else:
                valor = round(float(valor),2)
                catalogo[(produto.lower()).capitalize()] = valor
    
    cad_menu()


def cad_menu():
    
    os.system('cls')
    print(print_menu)
    opcao_cadastro = input('\tDigite a opção: ')
    print(opcao_cadastro)
    if str(opcao_cadastro) == '1':
        cadastro()

    elif str(opcao_cadastro) == '2':
        catalogo_prod()

    elif str(opcao_cadastro) == '3':
        #enviar_catalogo()
        deletar_item_catalago()

    elif str(opcao_cadastro) == '4':
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
    print("\t\nPara sair aperte 'S'")
    op = input('\tAperte a Tecla:').upper()
    if op == 'S':
        cad_menu()
    else:
        print('\tTecla invalida!!!')
        time.sleep(3)
        catalogo_prod()


def deletar_item_catalago():
    global catalogo
    os.system('cls')
    print(print_prod, end='')
    for i in  catalogo.keys():
        print(f"""
    |         {i:<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(catalogo[i]):<6s}                  |""", end=''
        )
    print(print_fim)
    apagar = str(input('\tDigite o nome do Item gostaria de deletar do catalogo: '))
    if apagar in catalogo.keys():
        catalogo.pop(apagar, None)
        os.system('cls')
        print(print_prod, end='')
        for i in  catalogo.keys():
            print(f"""
    |         {i:<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(catalogo[i]):<6s}                  |""", end=''
            )
        print(print_fim)
        print(f'\t{apagar} deletado com sucesso!')
        time.sleep(3)
        menu.menu_funcs()      

 
    
def enviar_catalogo():
    global catalogo
    catalogo = catalogo
    return catalogo
