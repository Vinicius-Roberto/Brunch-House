import os
from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'htmls'))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

if __name__ == "__main__":
    app.run(debug=True)