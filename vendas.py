carrinho = []
valorCarrinho = []
valorTotal = []
catalogo = {"graos" : 10.00 , "feijão": 20.00 , "arroz" : 45.50} # trocar pelo dicionario do cadastro de itens
fecha = "S" #joga o programa para dentro do laço do carrinho

print('''
    Bem vindo ao menu de vendas 
    
    Produtos disponiveis: 

    ''')

while fecha != "N":
    for i in  catalogo.keys() :
        print(f"\n{i}  {catalogo[i]} \n")   

    
    itemadd = (input("por favor digite o nome do produto a ser adicionado ? "))

    while not itemadd in catalogo: #verifica se o produto está cadastrado.
        print("produto não cadastrado")
        itemadd = (input("por favor digite o nome do produto a ser adicionado ?"))

    carrinho.append(itemadd)
    valorCarrinho.append(catalogo[itemadd])
    
    print ("carrinho atualizado: \n{}\n".format(carrinho))
    
    fecha = str(input("deseja adicionar mais intens? (S/N): ")).upper()

    while not fecha in ("S" , "N") : #verifica se o o usuario digitou certo a opção de checkout
        print("opção invalida")
        fecha = str(input("deseja adicionar mais intens? (S/N): ")).upper()
    
    #da linha 33 a 42 função de retirar itens do carrinho ainda em contrução
'''retirar = str(input("Deseja retirar algum item? (S/N) ")).upper()

while retirar != "N" :

        itemdel = str(input("Digite o nome do item a retirar "))
        carrinho.pop(carrinho.index(itemdel))
        valorCarrinho.pop(catalogo[itemdel])
        print ("carrinho atualizado: \n{}\n".format(carrinho))
        retirar = str(input("Deseja retirar algum item? (S/N) ")).upper()
print ("carrinho atualizado: \n{}\n".format(carrinho))'''

        
valorTotal = float(sum(valorCarrinho))

print("\n Resumo \n")
for i in carrinho:

    print('''
    {:<} R${:>}''' . format(i , catalogo[i]))

print(f"\nValor total é: R${valorTotal}\n ")