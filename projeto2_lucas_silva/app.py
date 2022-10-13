import os
from flask import Flask, url_for, redirect, render_template, request
import pandas as pd
from datetime import datetime

app = Flask(__name__)
catalogo = pd.read_csv('projeto2_lucas_silva/catalogo.csv', sep=',')
cart = pd.read_csv('projeto2_lucas_silva/cart.csv', sep=',', index_col='Produto')
total = 0

@app.route('/carrinho/<pag>')
def carrinho(pag):
    pag=int(pag)
    catalogo_pag = catalogo.iloc[12*(pag-1):12*pag]
    return render_template('carrinho.html', catalogo = catalogo_pag, pag=pag)

@app.route('/produto_adicionado/<produtos>/<valor>')
def teste(produtos , valor):
    if produtos in cart.index.values:
        cart.loc[produtos,"Quantidade"] = float(cart.loc[produtos,"Quantidade"]) + 1 
    else:
        cart.loc[produtos] =  [valor, 1, 0]
    cart.to_csv('projeto2_lucas_silva/cart.csv')       
    return redirect(request.referrer)

@app.route('/produto_excluido/<produtos>')
def excluir(produtos):
    cart.drop(produtos, inplace = True)
    cart.to_csv('projeto2_lucas_silva/cart.csv')  
    return redirect('/finalizar')
  
@app.route('/finalizar')
def finalizar():
    argumentos = request.args.to_dict()
    
    if len(argumentos) == 0:
        for index, row in cart.iterrows():
            cart.loc[index, "total"] = float(row["valor"]) * float(row["Quantidade"])      
    else: 
        for key in argumentos:
            cart.loc[key,"Quantidade"] = argumentos[key]
            cart.loc[key, "total"] = float(argumentos[key]) * float(cart.loc[key,"valor"])
    
    total_produto= (cart['Quantidade'].astype(float)*cart['valor'].astype(float))
    total= cart["total"].astype(float).sum()
    return render_template('Checkout.html' ,cart =cart, total = total)

@app.route('/obrigado')
def historico():
    df_historico = pd.read_csv('projeto2_lucas_silva/cart.csv', sep=',', index_col='Produto')
    df_historico['data']=datetime.today()
    df_sales =pd.read_csv('projeto2_lucas_silva/sales.csv',  sep=',', index_col='Produto')
    result = [df_historico, df_sales]
    df_result =pd.concat(result)
    df_result.to_csv('projeto2_lucas_silva/sales.csv')
       
    return 'deu certo'
    
if __name__ == "__main__":
    app.run(debug=True)
