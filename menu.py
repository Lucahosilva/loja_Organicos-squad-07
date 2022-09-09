# your_name=input("Qual é o seu nome? ")
#print("\n Prazer em lhe conhecer {}".format(your_name.capitalize()))


def menu_funcs():
	print("""
|--------------------------------------------------------------------------------------|""")
	print(
"""

		             Essas são minhas teclas:  
				
				[1] - Cadastro
				[2] - Vendas
				[3] - Relatório 
				[0] - Para SAIR 
	
""")
	print("""
|--------------------------------------------------------------------------------------|""")


menu_funcs()



first_choice= input ("            ---------------------Qual a tecla desejada?-----------------  ")

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
		
		print("""                  ----------------------------------------
                                                                           
                        lacunas pra preencher                              
                       Vendas                                             
			                                                               
		-------------------------------------------                       
		""")
	menu_vendas()
elif first_choice == "3":
    def relatorios():

        print("""
        
        Lacunas a preencher
        Relatórios
        
        """)
    relatorios()

	
    





