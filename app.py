from flask import Flask,render_template,request,redirect,url_for
from data.produtos import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/produtos')
def produtos():
    produtos = listar_produtos()
    return render_template('produtos.html',produtos=produtos)


@app.route('/produto',methods=['GET'])
def idex():
    return render_template('adicionar_produto.html')

@app.route('/produto',methods=['POST'])
def cadastrar():
    descricao = request.form['descricao']
    embalagem = request.form['embalagem']
    fornecedor = request.form['fornecedor']

    cadasdastrar_produto(descricao,embalagem,fornecedor)

    return redirect(url_for('produtos'))

@app.route('/excluir/<int:id>', methods=['GET'])
def excluir_produto(id):
    if id in produtos:
        del produtos[id]
        return redirect(url_for('produtos'))
    else:
        return "Produto não encontrado."


if __name__ == '__main__':
    app.run(debug=True)


