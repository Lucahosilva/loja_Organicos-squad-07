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

user = input("Digite seu nome: ")
print(f'Bem vindo {user}!!!\n\n{menu}')

#Chamar outras funções do menu 2
opcoes = ( 1 , 2 , 3 , 0)
