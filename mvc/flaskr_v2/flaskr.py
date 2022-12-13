from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, session, redirect, url_for, render_template

# USUARIO E SENHA do blog : admin
# Cria uma instância do App que é o nosso controlador
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

# Configura a conexão com o banco de dados
# Aqui estamos utilizando o sqlite em memória, caso você queira adicionar
# persistência basta alterr para um caminho de arquivo válido
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
bd = SQLAlchemy(app)


# Cria um modelo do Post do Blog
class Post(bd.Model):
    id = bd.Column(bd.Integer, primary_key=True)
    titulo = bd.Column(bd.String)
    texto = bd.Column(bd.String)

    def __init__(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto


# Cria e registra as rotas para as diferentes URL's do controlador
@app.route('/')
def exibir_entradas():
    entradas = Post.query.all()
    # Após realizar os procedimentos necesssário, chama a visualização correta
    return render_template('exibir_entradas.html', entradas=entradas)


@app.route('/inserir', methods=['POST'])
def inserir_entrada():
    novo_post = Post(request.form['titulo'], request.form['texto'])
    bd.session.add(novo_post)
    bd.session.commit()
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
    return redirect(url_for('exibir_entradas'))


# Executa o laço principal do programa
# você pode acessar a aplicação no endereço localhost:5000 no seu browser
if __name__ == '__main__':
    bd.create_all()
    app.run(debug=True)
