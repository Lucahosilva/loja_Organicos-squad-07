
from flask import Flask, url_for, redirect, render_template, request
import pandas as pd



app = Flask(__name__)
catalogo = pd.read_csv('projeto2_lucas_silva/catalogo.csv', sep=',')
cart = pd.DataFrame({"Produto":[],"valor":[], "Quantidade":[]})
cart.set_index('Produto', inplace = True)
total = 0

@app.route('/carrinho/<pag>')
def carrinho(pag):
    pag=int(pag)
    catalogo_pag = catalogo.iloc[12*(pag-1):12*pag]
    return render_template('carrinho.html', catalogo = catalogo_pag, pag=pag)

@app.route('/produto_adicionado/<produtos>/<valor>')
def teste(produtos , valor):
    if produtos in cart.index.values:
        cart.loc[produtos,"Quantidade"] += 1 
    else:
        cart.loc[produtos] =  [valor, 1 ]
    cart.to_csv('projeto2_lucas_silva/cart.csv')       
    return redirect(request.referrer)
    #return redirect ('/carrinho/1')

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
            cart.loc[index,"Quantidade"] = argumentos['qtd']
    else: 
        for key in argumentos:
            cart.loc[key,"Quantidade"] = argumentos[key]
            cart.loc[key, "total"] = float(argumentos[key]) * float(cart.loc[key,"valor"])
    
    total_produto= (cart['Quantidade'].astype(float)*cart['valor'].astype(float))
    total= cart["total"].astype(float).sum()
    return render_template('Checkout.html' ,cart =cart, total = total)
    
if __name__ == "__main__":
    app.run(debug=True)
