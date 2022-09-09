from curses.ascii import isdigit


boasvindas = """
|------------------------------------------------------------------------------------------------------------|
|                                                                                                            |
|                                         Seja bem vindo ao Organico’s !!!                                   |
|                                ----------------------------------------------------                        |
|                                                                                                            |
|------------------------------------------------------------------------------------------------------------|
"""

menu = """
|--------------------------------------------------------------------------------------------------|
|             Selecione o menu apertando as teclas sugeridas                                       |
|                                                                                                  |
|             Cadastro     - 1                                                                     |
|             Vendas       - 2                                                                     |                 
|             Relatórios   - 3                                                                     |
|             sair         - 0                                                                     |
|--------------------------------------------------------------------------------------------------|
"""

print(boasvindas)

catalogo = {}
user = input("Digite seu nome: ")
produto = ''
valor = ''

print(f'Bem vindo {user}!!!\n\n{menu}')

#Chamar outras funções do menu 2
opcoes = 0



def cadastro():
    global produto
    global valor
    global catalogo

    print('|--------------------------------------------------------------------------------------------------|')
    print('''                                                                                                                 
                Digite o nome do Produto ou \'x\' para sair: 
                ''')
    print('|--------------------------------------------------------------------------------------------------|')
    print('')
    produto= input('Nome do Produto: ')

    if produto.lower() == "x":
        print('Voltando ao menu principal')
        produto = 'x'
    elif produto.isalpha() == False:
        print('Entrada Inválida')
    else:
        while type(valor) != float:
            print('|--------------------------------------------------------------------------------------------------|')
            print(f'''  
                Qual o valor de {produto}?                                                            
                Substitua a Vírgula por '.' (ponto)                                                   
                (ou \'x\' para cancelar) : 
                ''')                                                         
            print('|--------------------------------------------------------------------------------------------------|',end='\n')
            print('')

            valor = input(f'Qual o valor de {produto}? : ')

            if valor.lower() == 'x':
                print('Voltando ao menu principal')
                valor = float(0)
                produto = 'x'
            elif valor.replace(".", "", 1).isdigit() == False:
                print('Entrada Inválida')
            else:
                valor = round(float(valor),2)
                catalogo[(produto.lower()).capitalize()] = valor
                produto = 'x'
    print('|--------------------------------------------------------------------------------------------------|')
    print('''   
                Opções-

                1- Cadastrar outro Produto
                2- Voltar ao menu anterior
                ''')
    print('|--------------------------------------------------------------------------------------------------|')
    opcao_cadastro = input('')
    if opcao_cadastro.isdigit() == False:
            print('Entrada Inválida')
    elif int(opcao_cadastro) == 1:
        produto = ''
        valor = ''
    elif int(opcao_cadastro) == 2:
        valor = ''
        produto = 'x'
    else:
        print('Entrada Inválida')
        produto = ''
        valor = ''
    
        

while produto != 'x':
    cadastro()

print(catalogo)

    
