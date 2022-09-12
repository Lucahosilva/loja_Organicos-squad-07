from pickletools import opcodes
import os
import menu
nome = ''
vendas = []
#---------------------- Impressões de formatação detexto--------------------------------------------#
relat = f'''
    |--------------------------------------------------------------------------------------------------|
    |                                  Vendas feita no dia.                                            |
    |                                                                                                  |
    |--------------------------------------------------------------------------------------------------|
    |         Produtos                                                     Preço                       |
    |                                                                                                  |'''

fim = """
    |--------------------------------------------------------------------------------------------------|
                """


def Relatorio(itens , user):
    global nome
    global vendas

    vendas = itens
    nome = user

    #--------------------------------Função para gerar relatorios---------------------------#
    os.system('cls')
    print(relat, end='')
    for i in range(len(vendas)):
        print(f"""
    |         {str(vendas[i][0]):<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(vendas[i][1]):<6s}                  |""", end=''
        )
    
    total = 0
    for i in range(len(vendas)):
        total += vendas[i][1]
    print(f"""
    |                                                                                                  |
    |         Total de vendas no Dia:.  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(total):<6s}                  |""", end=''
        )

    print(fim)
    sair(vendas, nome)

def sair(vendas, nome):
    print("\nPara Sair aperte 'X': ")
    qt = '1'
    while qt != 'X':
        qt = input("Tecla: ").upper()
        if qt == 'X':
            menu.menu_funcs(vendas)
        else:
            print('Opção invalida!!')
            os.system('cls')
            Relatorio(vendas, nome)

#--------------Final da opção 1---------------------------------------------------#

    #relatorio()
