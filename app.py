from flask import Flask, render_template, request
app = Flask(__name__)
from util.banco import insert, select, update, delete
@app.route("/")
def index():
    return render_template('index.html'), 200

@app.route("/refeicoes.html")
def refeicoes():
    resultado = select()
    if resultado == None:
         return render_template('refeicoes.html'), 200
    else:
        return render_template('refeicoes.html', resultado=resultado), 200

@app.route("/valores.html")
def valores():
    return render_template('valores.html'), 200

@app.route('/resultado', methods=["GET", "POST"])
def resultado():
    if request.form.get("incluir"):
        codigo = request.form['codigo']
        nome = request.form["nome"]
        valor = request.form['valor']
        date = request.form['date']
        hinicio = request.form['hinicio']
        htermino = request.form['htermino']
        insert(codigo, nome, valor, date, hinicio, htermino)
        return render_template('/resultado.html'), 200
    elif request.form.get('alterar'):
        codigo = request.form['codigo']
        nome = request.form['nome']
        valor = request.form['valor']
        date = request.form['date']
        hinicio = request.form['hinicio']
        htermino = request.form['htermino']
        print(f'dados para o update = {codigo}, {nome}, {valor}, {date},{hinicio}, {htermino}')
        update(codigo, nome, valor, date, hinicio, htermino)
        return render_template('/resultado.html'), 200
    elif request.form.get('excluir'):
        codigo = request.form['codigo']
        delete(codigo)
        return render_template('/resultado.html'), 200
    else:
        return "Não Definido", 200

@app.route("/relatorios.html")
def relatorios():
    return render_template('relatorios.html'), 200

app.run(host = '0.0.0.0', debug =True)