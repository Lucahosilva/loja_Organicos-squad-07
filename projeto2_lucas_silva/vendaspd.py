import pandas as pd


cart = pd.DataFrame({"Produto:":[],"valor":[], "Quantidade":1})

total = 0


def add_cart():
    cart.loc[len(cart)] = 'banana', float(10), 1 #Substituir pelas informações do catalogo do produto na hora que apertarem adicionar ao cart no cart.html
    print(cart)
    total = cart["valor"].sum()
    print(total)
cart.to_csv("cart.csv", index=False)



