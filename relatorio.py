from pickletools import opcodes
import os

nome = 'William'
#---------------------- Impressões de formatação detexto--------------------------------------------#
relat = f'''
|--------------------------------------------------------------------------------------------------|
|                             Vendas feita pelo usuario: {nome:<10s}                                |
|                                                                                                  |
|--------------------------------------------------------------------------------------------------|
|         Produtos                                                     Preço                       |
|                                                                                                  |'''

fim = """
|--------------------------------------------------------------------------------------------------|
            """

menu_relat = """
|--------------------------------------------------------------------------------------------------|
|             Selecione o menu apertando as teclas sugeridas                                       |
|                                                                                                  |
|             Imprimir relátorio        - 1                                                        |
|             Para sair                 - S                                                        |
|--------------------------------------------------------------------------------------------------|
"""
#---------------------------------------------------------------------------------------------------#


vendas = {   'Açucar': 10.20,
            'Pinga': 2.20,
            'Manteiga': 7.80,
            'Mel': 10.00,
            'Vinagre': 3.50,
            'Escova dental': 12.50,
            'Coca-cola': 9.00,
            'Guarana antartica': 7.00,
        }
opcoes = 1

#--------------------------------Função para gerar relatorios---------------------------#
def relatorio():
    os.system('cls')
    print(menu_relat)
    global opcoes

#-----------------While para verificar a função digitada---------------------------#
    while not opcoes == 0:
        print('\n')
        opcoes = input("Digite uma opção: ")

#----------------Funções da opção 1 quando selecionada-----------------------------#
        if opcoes == '1':
            os.system('cls')
            print(relat, end='')
            for i in vendas.keys():
                print(f"""
|         {i:<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(vendas[i]):<6s}                  |""", end=''
            )
            print(fim)
            print(menu_relat)
#--------------Final da opção 1---------------------------------------------------#

#--------------Função quando usuário pede para sair--------------------------------#
        elif opcoes.upper() == 'S':
            os.system('cls')
            print(f"Obrigado {nome}\n\n")
            break

#------------Verificação de teclas que não são opções----------------------------#
        else:
            os.system('cls')
            print("opção não valida, Digite uma das opções a seguir")
            print(menu_relat)
    

# chamar relatorio
relatorio()
