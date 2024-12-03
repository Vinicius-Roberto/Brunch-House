import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html")

@app.route("/detalhes-produtos")
def detalhes():
    return render_template("detalhes-produtos.html")

if __name__ == "__main__":
    app.run(debug=True)
