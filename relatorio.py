from pickletools import opcodes


relat = """
|--------------------------------------------------------------------------------------------------|
|             Selecione o menu apertando as teclas sugeridas                                       |
|                                                                                                  |
|             Imprimir relátorio        - 1                                                        |
|             Para sair                 - 0                                                        |
|--------------------------------------------------------------------------------------------------|
"""


vendas = {   'Açucar': 10.20,
            'Pinga': 2.20,
            'Manteiga': 7.80,
            'Mel': 10.00,
            'Vinagre': 3.50,
            'Escova dental': 12.50,
            'Coca-cola': 9.00,
            'Guarana antartica': 7.00,
        }
opcoes = 11
nome = 'William'
print(len(vendas.keys()))
def relatorio():
    print(relat)
    global opcoes

    while not opcoes == 0:
        opcoes = int(input("Digite uma opção: "))

        if opcoes == 1:
            print(f'''
|--------------------------------------------------------------------------------------------------|
|                             Vendas feita pelo usuario: {nome}                                   |
|--------------------------------------------------------------------------------------------------|
|                                                                                                  |''',end=''
            )

            for i in vendas.keys():
                print(f"""
|         Produto:    {i:<20s} ........................... Valor:    {str(vendas[i]):<6s}            |
|                                                                                                  |""", end=''
            )
        

        elif opcoes == 0:
            print("Sair")
            break
        else:
            print("opção não valida")
        print("""
|--------------------------------------------------------------------------------------------------|
        \n\n""")
    

# chamar relatorio
relatorio()
