
from flask import Flask, url_for, redirect, render_template, request
import pandas as pd


app = Flask(__name__)
catalogo = pd.read_csv('projeto2\catalogo.csv', sep=';')
cart = pd.DataFrame({"Produto:":[],"valor":[], "Quantidade":1})

#print(catalogo)

@app.route('/carrinho/<pag>')
def carrinho(pag):
    pag=int(pag)
    catalogo_pag = catalogo.iloc[6*(pag-1):6*pag]
    return render_template('carrinho.html', catalogo = catalogo_pag, pag=pag)

@app.route('/produto_adicionado')
def teste():
        cart.loc[len(cart)] = 'banana', float(10), 1 #Substituir pelas informações do catalogo do produto na hora que apertarem adicionar ao carrinho no carrinho.html
        print(cart)
        mensagem = "deu certo"
        return mensagem 
        redirect ('/carrinho/<0>')

    


@app.route('/finalizar')
def finalizar():
    return render_template('Checkout.html')





if __name__ == "__main__":
    app.run(debug=True)