import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    df = pd.read_csv('tabela_brunchhouse.csv')

    # Obtendo os últimos 5 produtos
    ultimos_5 = df.tail(5).to_dict('records')

    # Obtendo os 5 antepenúltimos produtos
    antepenultimos_5 = df[5:10].to_dict('records')

    # Enviando os dados para o template
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
    return render_template("carrinho.html")

@app.route("/detalhes-produtos/<int:id>")
def detalhes(id):
    df = pd.read_csv('tabela_brunchhouse.csv')
    produto = df[df['id'] == id].to_dict('records')
    if produto:
        produto = produto[0]  # Acessa o primeiro (e único) elemento da lista
        return render_template("detalhes-produtos.html", produto=produto)
    else:
        # Produto não encontrado
        return "Produto não encontrado"

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
