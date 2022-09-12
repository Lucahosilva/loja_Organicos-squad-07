
import os
import time
import menu

print_addCar = """
    |----------------------------|
    |     Itens no carrinh       |
    |----------------------------|
"""
print_carr ='''
    |--------------------------------------------------------------------------------------------------|
    |                                    Total de produtos comprados                                   |
    |--------------------------------------------------------------------------------------------------|
    |         Produtos                                                     Preço                       |
    |                                                                                                  |'''

print_prod ='''
    |--------------------------------------------------------------------------------------------------|
    |                                      Produtos cadastrados                                        |
    |--------------------------------------------------------------------------------------------------|
    |         Produtos                                                     Preço                       |
    |                                                                                                  |'''

print_fim =  """
    |--------------------------------------------------------------------------------------------------|
"""
#Variaveis--------------
catalogo = {}
carrinho = []
total = 0

def Print_catalogo():
    global catalogo
    os.system('cls')
    print(print_prod, end='')
    for i in  catalogo.keys():
        print(f"""
    |         {i:<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(catalogo[i]):<6s}                  |""", end=''
        )
    print(print_fim)     

def Vendas(itens):
    global catalogo
    global carrinho
    catalogo = itens
    global total
    fecha = "S"

    while fecha != "N":
        os.system('cls')
        Print_catalogo()
        itemadd = (input("por favor digite o nome do produto a ser adicionado: "))
        while not itemadd in catalogo: #verifica se o produto está cadastrado.
            os.system('cls')
            Print_catalogo()
            print("produto não cadastrado")
            itemadd = (input("por favor digite o nome do produto a ser adicionado: "))
        carrinho.append([itemadd, catalogo[itemadd] ])
          
        print(print_addCar, end='')
        for i in range(len(carrinho)):
            print(f"""
        Item: {carrinho[i][0]}       """,end='')
        
        total = 0
        for i in range(len(carrinho)):
            total += carrinho[i][1]
        print(f"""
        \n        Total        R$: {total:.2f}""", end=''
    )
            
        fecha = str(input("\n\ndeseja adicionar mais intens? (S/N): ")).upper()
        #return carrinho
    menu.menu_funcs(carrinho)

def Deletar():
    print('Deletar')

    print(carrinho)

    itemDelete = int(input("Favor informe qual ID deseja deletar: "))
    while itemDelete not in carrinho[0]:
        print("produto não encontrado no carrinho ") #verifica se o item está no carrinho
        itemDelete = input("Favor informe qual ID deseja deletar: ")
    carrinho.pop(itemDelete)

    for i in range(len(carrinho)):
            print(f"""
        Item: {carrinho[i][0]}       """,end='')
        
    total = 0

    for i in range(len(carrinho)):
         total += carrinho[i][1]
    print(f"""
        \n        Total        R$: {total:.2f}""", end='')


    Print_catalogo()

