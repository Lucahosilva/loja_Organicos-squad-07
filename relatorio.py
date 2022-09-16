from pickletools import opcodes
import os
import menu
import time
nome = ''
vendas = []
#---------------------- Impressões de formatação detexto--------------------------------------------#

print_catalogo_vazio = """
	|--------------------------------------------------------------------------------------------------|
	|                                  Seja bem vindo ao Organico’s !!!                                |
	|                       ----------------------------------------------------                       |
	|         Para imprimir o relátorio, o usuário precisa cadastrar uma venda.                        |
	|         Não existe vendas cadastradas.                                                           |
	|                                                                                                  |
	|--------------------------------------------------------------------------------------------------|
	"""

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
    if len(vendas) <=0:
        print(print_catalogo_vazio)
        time.sleep(3)
        menu.menu_funcs(vendas)
    else:

        os.system('cls')
        print(relat, end='')
        for i in range(len(vendas)):
            print(f"""
    |         {str(vendas[i][0]):<20s}.  .  .  .  .  .  .  .  .  .  .  .  .  . R$: {str(vendas[i][1]):<6s}                  |""", end=''
            )
        
        total = 0
        for i in range(len(vendas)):
            total += vendas[i][1]
        
        maior = 0
        for i in range(len(vendas)):
            if float(maior) < vendas[i][1]:
                maior = vendas[i][1]
        
        menor = 999999999999
        for i in range(len(vendas)):
            if float(menor) > vendas[i][1]:
                menor = vendas[i][1]
        print(f"""
    |--------------------------------------------------------------------------------------------------|
    |             Total de vendas | Item com maior valor | Item com menor valor | Ticket médio         | 
    |             R$: {str(total):<6s}      | R$: {maior:.2f}            | R$: {menor:.2f}             | R$: {total / len(vendas):.2f}             |""", end=''
            )
        print(fim)
        sair(vendas, nome)

def sair(vendas, nome):
    print("\nPara Sair aperte 'S': ")
    qt = '1'
    while qt != 'S':
        qt = input("Tecla: ").upper()
        if qt == 'S':
            menu.menu_funcs(vendas)
        else:
            print('Opção invalida!!')
            os.system('cls')
            Relatorio(vendas, nome)

#--------------Final da opção 1---------------------------------------------------#

    #relatorio()