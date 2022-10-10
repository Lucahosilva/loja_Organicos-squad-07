
from flask import Flask, url_for, redirect, render_template, request
import pandas as pd



app = Flask(__name__)
catalogo = pd.read_csv('projeto2_lucas_silva/catalogo.csv', sep=',')
cart = pd.DataFrame({"Produto":[],"valor":[], "Quantidade":[]})
total = 0

@app.route('/carrinho/<pag>')
def carrinho(pag):
    pag=int(pag)
    catalogo_pag = catalogo.iloc[6*(pag-1):6*pag]
    return render_template('carrinho.html', catalogo = catalogo_pag, pag=pag)

@app.route('/produto_adicionado/<produtos>/<valor>')
def teste(produtos , valor):
        cart.loc[len(cart)] = produtos , valor, 1 
        cart.to_csv('projeto2_lucas_silva/cart.csv')       
        return redirect ('/carrinho/1')

@app.route('/produto_excluido/<produtos>')
def excluir(produtos):
    cart.drop(produtos, inplace = True)
    cart.to_csv('projeto2_lucas_silva/cart.csv')  
    return redirect('Checkout.html', produtos = produtos)
    
@app.route('/finalizar')
def finalizar():
    #cart['valor']=float(cart['valor'])
    total= cart['valor']
    return render_template('Checkout.html' ,cart =cart, total = total)
    
if __name__ == "__main__":
    app.run(debug=True)