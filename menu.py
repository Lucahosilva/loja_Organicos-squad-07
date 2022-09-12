import os
import cadastro
import vendas
import relatorio
import teste

#---------------------------------------Menu inicial---------------------------------------------------#

print_boasvindas = """
	|--------------------------------------------------------------------------------------------------|
	|                                                                                                  |
	|                                  Seja bem vindo ao Organico’s !!!                                |
	|                       ----------------------------------------------------                       |
	|                                                                                                  |
	|--------------------------------------------------------------------------------------------------|
	"""

print_menu = """
	|--------------------------------------------------------------------------------------------------|
	|             Selecione o menu apertando as teclas sugeridas                                       |
	|                                                                                                  |
	|             Cadastro     -  1                                                                    |
	|             Vendas       -  2                                                                    |
	|             Relatórios   -  3                                                                    |
	|             sair         - 'S'                                                                   |
	|--------------------------------------------------------------------------------------------------|
	"""
catalogo = { }
carrinho = []
user = ''

def Menu_inicial():
	global user
	os.system('cls')
	print(print_boasvindas)
	user = input("\tDigite seu nome: ")
	menu_funcs()


def menu_funcs(itens = []):
	global carrinho
	carrinho = itens
	global catalogo
	os.system('cls')
	print(print_menu)

	first_choice = 0
	while first_choice != 'S':
		first_choice= input ('\tTecla: ')

		if first_choice.upper() == "S":
			os.system('cls')
			print(f"{user}, agradeço sua companhia e espero que tenha ajudado.")
			exit()

		elif first_choice == "1":
			os.system('cls')
			catalogo = cadastro.enviar_catalogo()
			cadastro.cad_menu()
			

		elif first_choice == "2":
			os.system('cls')
			Menu_vendas()

		elif first_choice == "3":
			os.system('cls')
			Menu_relatorio()

		else:
			os.system('cls')
			print('\tPor favor, aperte uma das teclas sugeridas!!!')
			print(print_menu)

	

#----------------------------------------- Menu Vendas -----------------------------------------#

print_menu_car ='''
    |--------------------------------------------------------------------------------------------------|
    |                                    Escolha uma função                                            |
    |--------------------------------------------------------------------------------------------------|
    |        Adicionar item - 1                Deletar item - 2                   Sair - X             |
    |--------------------------------------------------------------------------------------------------|'''


def Menu_vendas():
	global catalogo
	global carrinho
	print(print_menu_car)
	func = input('\tEscolha uma Função: ')
	if func == '1':
		carrinho = vendas.Vendas(catalogo)

	if func == '2':
		vendas.Deletar()


#----------------------------------------- Menu Reltorios -----------------------------------------#

menu_relatorio = """
    |--------------------------------------------------------------------------------------------------|
    |             Selecione uma função apertando as teclas sugeridas                                   |
    |                                                                                                  |
    |             Imprimir relátorio        - 1                                                        |
    |             Para sair                 - S                                                        |
    |--------------------------------------------------------------------------------------------------|
    """
def Menu_relatorio():
	global carrinho
	global user
	os.system('cls')
	print(menu_relatorio)
	func = input('\tEscolha uma Função: ')
	if func == '1':
		carrinho = relatorio.Relatorio(carrinho, user)

	if func == 'S':
		print('Saindo!!!')
		menu_funcs()
		
