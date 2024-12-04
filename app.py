import os
from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    df = pd.read_csv('tabela_brunchhouse.csv')
    ultimos_5 = df.tail(5).to_dict('records')
    antepenultimos_5 = df[5:10].to_dict('records')
    return render_template("index.html", produtoDestaque=ultimos_5, produtoData=antepenultimos_5)

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

@app.route("/produtos")
def produtos():
    df = pd.read_csv('tabela_brunchhouse.csv')
    produtos = df.to_dict('records')
    return render_template('produtos.html', produtos=produtos)

@app.route("/carrinho")
def carrinho():
    df = pd.read_csv('tabela_brunchhouse.csv')
    carrinho_produtos = df[df['carrinho'] > 0]
    carrinho_produtos = carrinho_produtos.to_dict('records')

    return render_template("carrinho.html", produtos=carrinho_produtos)

@app.route("/detalhes-produtos/<int:id>")
def detalhes(id):
    df = pd.read_csv('tabela_brunchhouse.csv')
    produto = df[df['id'] == id].to_dict('records')
    if produto:
        produto = produto[0]
        return render_template("detalhes-produtos.html", produto=produto)
    else:
        return "Produto não encontrado"

@app.route("/adicionar-ao-carrinho/<int:id>", methods=["POST"])
def adicionar_ao_carrinho(id):
    df = pd.read_csv('tabela_brunchhouse.csv')
    produto = df[df['id'] == id]

    if not produto.empty:
        df.loc[produto.index, 'carrinho'] += 1
        df.to_csv('tabela_brunchhouse.csv', index=False)
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'Produto não encontrado'})

@app.route("/remover-do-carrinho/<int:id>", methods=["POST"])
def remover_do_carrinho(id):
    df = pd.read_csv('tabela_brunchhouse.csv')
    produto = df[df['id'] == id]

    if not produto.empty:
        # Verificar se a quantidade é maior que zero
        if produto['carrinho'].values[0] > 0:
            df.loc[produto.index, 'carrinho'] -= 1
            df.to_csv('tabela_brunchhouse.csv', index=False)
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'Produto já está com quantidade zero'})
    else:
        return jsonify({'error': 'Produto não encontrado'})
        
@app.route("/produtos-destaque")
def destaque():
    return render_template("produto-destaque.html")

@app.route("/produtos-especiais")
def especiais():
    return render_template("produtos-especiais.html")

@app.route("/pagamento")
def pagamento():
    return render_template("pagamento.html")

@app.route("/cadastro-cartao")
def cadastro():
    return render_template("cadastrocartao.html")

if __name__ == "__main__":
    app.run(debug=True)
