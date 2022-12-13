import sqlite3
from flask import Flask, request, session, redirect, url_for, render_template

# USUARIO E SENHA do blog : admin
# Cria uma instância do App que é o nosso controlador
app = Flask(__name__)
app.secret_key = 'key'


# Cria e gerencia o Banco de dados que será nosso Modelo
# Em aplicações maiores teriamos classes de modelo reais
def criar_bd():
    bd = conectar_bd()
    with app.open_resource('esquema.sql') as sql:
        bd.cursor().executescript(sql.read().decode())
    bd.commit()
    bd.close()


def conectar_bd():
    return sqlite3.connect('./flaskr.db')


# Cria e registra as rotas para as diferentes URL's do controlador
@app.route('/')
def exibir_entradas():
    sql = '''select titulo, texto from entradas order by id desc'''
    con = conectar_bd()
    cur = con.execute(sql)
    entradas = [dict(titulo=titulo, texto=texto)
                for titulo, texto in cur.fetchall()]
    con.close()
    # Após realizar os procedimentos necesssário, chama a visualização correta
    return render_template('exibir_entradas.html', entradas=entradas)


@app.route('/inserir', methods=['POST'])
def inserir_entrada():
    sql = '''insert into entradas (titulo, texto) values (?, ?)'''
    con = conectar_bd()
    con.execute(sql, [request.form['titulo'], request.form['texto']])
    con.commit()
    con.close()
    # Após realizar os procedimentos necesssário, chama a visualização correta
    return redirect(url_for('exibir_entradas'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            erro = 'Usuário inválido'
        elif request.form['password'] != 'admin':
            erro = 'Senha inválida'
        else:
            session['logado'] = True
            return redirect(url_for('exibir_entradas'))
    # Após realizar os procedimentos necesssário, chama a visualização correta
    return render_template('login.html', erro=erro)


@app.route('/logout')
def logout():
    session.pop('logado', None)
    # Após realizar os procedimentos necesssário, chama a visualização correta
    return redirect(url_for('exibir_entradas'))


# Executa o laço principal do programa
# você pode acessar a aplicação no endereço localhost:5000 no seu browser
if __name__ == '__main__':
    criar_bd()
    app.run(debug=True)
