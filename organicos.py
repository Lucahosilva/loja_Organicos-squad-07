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
print('\n')
print(f'Bem vindo {user}!!!\n{menu}')

#Chamar outras funções do menu 2
<<<<<<< HEAD

def relatorio():
    fo
=======
opcoes = 0


# your_name=input("Qual é o seu nome? ")
#print("\n Prazer em lhe conhecer {}".format(your_name.capitalize()))


def menu_funcs():
	print("""
		Essas são minhas funções:
			(1) = Cadastro
			(2) = Vendas
			(3) = Relatório
			(0) = Para SAIR

	""")
	
menu_funcs()


first_choice= input ("Qual a função desejada? ")

if first_choice == "0":
	print("{}, agradeço sua companhia e espero que tenha ajudado.".format(your_name.capitalize()))
	exit()

elif first_choice == "1":

	def menu_organics():
		
		print("""

        lacunas pra preencher
        Cadastro

			
		""")
	menu_organics()

elif first_choice == "2":

	def menu_vendas():
		
		print("""

        lacunas pra preencher
        Vendas
			
		""")
	menu_vendas()
elif first_choice == "3":
    def relatorios():

        print("""
        
        Lacunas a preencher
		Relatório
        
        """)
    relatorios()

	


    

>>>>>>> b4f7de71db32d05c0db0d5649f3516480e367e19
