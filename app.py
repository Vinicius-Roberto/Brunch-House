import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

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

@app.route("/detalhes-produtos")
def detalhes():
    return render_template("detalhes-produtos.html")

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
