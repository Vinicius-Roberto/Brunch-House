import os
from flask import Flask, render_template

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
    return render_template("produtos.html")

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

if __name__ == "__main__":
    app.run(debug=True)
