
from flask import Flask, url_for, redirect, render_template, request
import pandas as pd


app = Flask(__name__)
catalogo = pd.read_csv('projeto2_lucas_silva/catalogo.csv', sep=';')
cart = pd.DataFrame({"Produto:":[],"valor":[], "Quantidade":[]})

#print(catalogo)

@app.route('/carrinho/<pag>')
def carrinho(pag):
    pag=int(pag)
    catalogo_pag = catalogo.iloc[6*(pag-1):6*pag]
    return render_template('carrinho.html', catalogo = catalogo_pag, pag=pag)

@app.route('/produto_adicionado/<produto>/<valor>')
def teste(produto , valor):
        cart.loc[len(cart)] = produto , valor, 1 
        cart.to_csv('projeto2_lucas_silva/cart.csv')
       
        return redirect ('/carrinho/1')

        
    


@app.route('/finalizar')
def finalizar():
    return render_template('Checkout.html')





if __name__ == "__main__":
    app.run(debug=True)