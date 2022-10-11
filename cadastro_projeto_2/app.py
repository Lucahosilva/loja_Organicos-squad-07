from flask import Flask, redirect, render_template, request, url_for
from flask.helpers import flash
import pandas as pd
import time

app = Flask(__name__)
app.secret_key = 'super secret'
catalogo = pd.read_csv('catalogo.csv', index_col='produtos')
itens_deletados = pd.read_csv('itens_deletados.csv', index_col='produtos')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', catalogo = catalogo)

@app.route('/cadastro/<string:nome_produto>')
def editar(nome_produto):
    nome_produto = nome_produto.replace('_', ' ')
    return render_template('editar.html',
                                nome_produto = nome_produto,
                                valor = catalogo.loc[nome_produto]['valor'],
                                quantidade = catalogo.loc[nome_produto]['quantidade']
                                )


@app.route('/alteracoes_produto')
def altera_item():
    argumentos = request.args.to_dict()

    antigo_nome = argumentos['antigo_nome']
    novo_nome = argumentos["novo_nome"]
    quantidade = argumentos["quantidade"]
    preco = argumentos["preco"]

    catalogo.loc[antigo_nome, 'quantidade'] = quantidade
    catalogo.loc[antigo_nome, 'valor'] = preco
    catalogo.rename(index={antigo_nome: novo_nome}, inplace=True)
    catalogo.to_csv('catalogo.csv')
    time.sleep(2)
    flash('Produto alterado com sucesso !', 'alert alert-success')
    return redirect('/cadastro')

@app.route('/deletar_produto/<string:nome_produto>')
def deletar(nome_produto):

    quantidade = catalogo.loc[nome_produto, 'quantidade']
    preco = catalogo.loc[nome_produto, 'valor']
    itens_deletados.loc[nome_produto] = [quantidade, preco]

    catalogo.drop(nome_produto, inplace=True)

    itens_deletados.to_csv('itens_deletados.csv')
    catalogo.to_csv('catalogo.csv')
    flash(f'Produto {nome_produto} Deletado !', 'alert delete-sucess')
    return redirect('/cadastro')

@app.route('/cadastro_filtro_preco_crescente')
def filtro_pcrescente():
    return render_template('cadastro.html', catalogo = catalogo.sort_values(by=['valor']))

@app.route('/cadastro_filtro_preco_decrescente')
def filtro_pdecrescente():
    return render_template('cadastro.html', catalogo = catalogo.sort_values(by=['valor'], ascending=False))

@app.route('/cadastro_filtro_quantidade_decrescente')
def filtro_qcrescente():
    return render_template('cadastro.html', catalogo = catalogo.sort_values(by=['quantidade'], ascending=False))

@app.route('/cadastro_filtro_quantidade_crescente')
def filtro_qdecrescente():
    return render_template('cadastro.html', catalogo = catalogo.sort_values(by=['quantidade']))

@app.route('/cadastro_filtro_alfabetico')
def filtro_alfabetico():
    return render_template('cadastro.html', catalogo = catalogo.sort_index())

@app.route('/cadastro_pesquisa')
def pesquisa():
    argumentos = request.args.to_dict()
    mascara = catalogo[catalogo.index.str.contains(argumentos['pesquisa'])]
    return render_template('cadastro.html',catalogo = mascara)
   
   
@app.route('/recuperacao')
def recove():
    return render_template('recuperacao_prod.html',itens_deletados = itens_deletados)

@app.route('/recuperacao_pesquisa')
def pesquisa_recover():
    argumentos = request.args.to_dict()
    mascara = itens_deletados[itens_deletados.index.str.contains(argumentos['pesquisa'])]
    return render_template('recuperacao_prod.html',itens_deletados = mascara)

@app.route('/recuper_para_cad/<id>')
def restauracao(id):

    quantidade = itens_deletados.loc[id, 'quantidade']
    preco = itens_deletados.loc[id, 'valor']

    catalogo.loc[id] = [quantidade, preco]

    itens_deletados.drop(id, inplace=True)

    itens_deletados.to_csv('itens_deletados.csv')
    catalogo.to_csv('catalogo.csv')

    flash(f'Produto {id} Recuperado com sucesso !', 'alert alert-success')
    return redirect('/recuperacao')


# rotas divino 

@app.route('/listar')
def listar():
    argumento = request.args.to_dict()
    produto = argumento['produto']
    preco = argumento['preco']
    quantidade = argumento['quantidade']
    catalogo.loc[produto]=[quantidade, preco]
    catalogo.to_csv('catalogo.csv')
    flash(f'{produto} adicionado com sucesso !', 'alert alert-success')
    return redirect('/cadastro')


if __name__ == "__main__":
    app.run(debug=True)

