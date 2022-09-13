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
    |       Id             Produtos                                                   Preço            |
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
    for i, produto in  enumerate(catalogo):
        print(f"""
    |        {i}    .   .    {produto:<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  R$: {str(catalogo[produto]):<6s}       |""", end=''
        )
    print(print_fim)     

def Vendas(itens):
    global catalogo
    global carrinho
    catalogo = itens
    global total
    fecha = "S"
    lista_de_venda = [] # mudança para nome de item por indice no carrinho de vendas

    for item in catalogo: # mudança para nome de item por indice no carrinho de vendas
        lista_de_venda.append(item) # mudança para nome de item por indice no carrinho de vendas
    
    while fecha != "N":
        os.system('cls')
        Print_catalogo()
        itemadd = input("por favor digite o ID do produto a ser adicionado: ")
        if itemadd.upper()== "S":
            fecha= "N"
            menu.menu_funcs(carrinho)
     
        while not itemadd.isdigit() or  int(itemadd) > len(lista_de_venda) - 1 : #verifica se o produto está cadastrado. # mudança para nome de item por indice no carrinho de vendas
            
            os.system('cls')
            Print_catalogo()
            print("produto não cadastrado")
            itemadd = (input("por favor digite o código do produto a ser adicionado: "))

        print(len(lista_de_venda))
        carrinho.append([lista_de_venda[(int(itemadd))], catalogo[(lista_de_venda[int(itemadd)])]]) # mudança para nome de item por indice no carrinho de vendas
            #valorCarrinho.append(catalogo[itemadd])
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
    while itemDelete > len(carrinho) :
        print("produto não encontrado no carrinho ") #verifica se o item está no carrinho
        itemDelete = int(input("Favor informe qual ID deseja deletar: "))
    carrinho.pop(itemDelete)

    print(f'''
    item Deletado com sucesso
    ''')

    for i in range(len(carrinho)):
            print(f"""
        Item: {carrinho[i][0]}       """,end='')
        
    total = 0

    for i in range(len(carrinho)):
         total += carrinho[i][1]
    print(f"""
        \n        Total        R$: {total:.2f}""", end='')

    
    time.sleep(3)
    menu.menu_funcs(carrinho)



    

