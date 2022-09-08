carrinho = []
valorTotal = []
lista_produtos = {"graos" : 10.00 , "feijão": 20 , "arroz" : 45.50}
final = "S" #joga o programa para dentro do laço do carrinho

while final != "N":
    print(f'''
    Produtos disponiveis: 
    {lista_produtos}
    ''')
    itemadd = (input("por favor digite o nome do produto a ser adicionado ?"))
    carrinho.append(lista_produtos[itemadd])
    print ("carrinho atualizado: " , carrinho)

    final = str(input("deseja adicionar mais intens? (S/N)")).upper()


valorTotal = sum(carrinho)
print("o valor final é " , valorTotal)






