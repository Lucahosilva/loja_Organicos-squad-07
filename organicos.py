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
    produto = input(''' 
 |--------------------------------------------------------------------------------------------------|                
                                                                                                  
                Digite o nome do Produto ou \'x\' para sair:                                          
                                                                                                 
 |--------------------------------------------------------------------------------------------------|

 Produto : ''')
    if produto.lower() == 'x':
        print('Voltando ao menu principal')
        produto = 'x'
    elif produto.isalpha() == False:
        print('Entrada Inválida')
    else:
        valor = input(f'''
 |--------------------------------------------------------------------------------------------------|                
            Qual o valor de {produto}?                                                            
            Substitua a Vírgula por '.' (ponto)                s                                   
            (ou \'x\' para cancelar) :                                                            
 |--------------------------------------------------------------------------------------------------|

 Qual o valor de {produto}? :  ''')
        if valor.lower() == 'x':
            print('Voltando ao menu principal')
            del catalogo[produto]
            produto = 'x'
            #código para voltar para o menu
        elif produto.isdigit() == False:
            print('Entrada Inválida')
        else:
            catalogo[(produto.lower()).capitalize] = float(valor)
            produto = 'x'

while produto != 'x':
    cadastro()

    
