carrinho = []
valorCarrinho = []
valorTotal = []
lista_produtos = {"graos" : 10.00 , "feijão": 20 , "arroz" : 45.50}
final = "S" #joga o programa para dentro do laço do carrinho

while final != "N":
    print(f"Produtos disponiveis: \n{lista_produtos}" , "\n")
    itemadd = (input("por favor digite o nome do produto a ser adicionado ?"))

    while not itemadd in lista_produtos: #verifica se o produto está cadastrado.
        print("produto não cadastrado, por favor digite outro")
        itemadd = (input("por favor digite o nome do produto a ser adicionado ?"))

    carrinho.append(itemadd)
    valorCarrinho.append(lista_produtos[itemadd])
    print ("carrinho atualizado: \n" , carrinho , )
    
    final = str(input("deseja adicionar mais intens? (S/N)")).upper()


valorTotal = sum(valorCarrinho)
print(f'''
Resumo: 
{carrinho}
Valor total é: {valorTotal}

''')






