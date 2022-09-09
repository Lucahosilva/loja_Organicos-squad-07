carrinho = []
valorCarrinho = []
valorTotal = []
catalogo = {"graos" : 10.00 , "feijão": 20 , "arroz" : 45.50} # trocar pelo dicionario do cadastro de itens
fecha = "S" #joga o programa para dentro do laço do carrinho

while fecha != "N":

    for i in  catalogo.keys() :
        print(f"{i}  {catalogo[i]}")      


    itemadd = (input("por favor digite o nome do produto a ser adicionado ?"))

    while not itemadd in catalogo: #verifica se o produto está cadastrado.
        print("produto não cadastrado")
        itemadd = (input("por favor digite o nome do produto a ser adicionado ?"))

    carrinho.append(itemadd)
    valorCarrinho.append(catalogo[itemadd])
    print ("carrinho atualizado: \n{}\n".format(carrinho))
    
    fecha = str(input("deseja adicionar mais intens? (S/N): ")).upper()


valorTotal = float(sum(valorCarrinho))

print("\n Resumo \n")
for i in carrinho:

    print('''
    {:<} R${:>}''' . format(i , catalogo[i]))

print(f"\nValor total é: R${valorTotal}\n ")