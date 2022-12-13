# Padrão Modelo-Visualização-Controle (MVC)

Exemplos de uso do padrão de projeto Modelo-Visualização-Controlador

## Jogo da forca (Python)

Um exemplo de construção de jogo utilizando o padrão MVC é um jogo da forca, que pode ser encontrado [nesse repositório do Github](https://github.com/manuphatak/python_hangman). Dentro do diretório `hangman` é possível encontrar os arquivos `model.py` (Modelo), `view.py` (Visualização) e `controller.py` (Controlador).

## Sistema de cadastro de pessoas (Python)

O arquivo `pessoas.py` mostra um exemplo de sistema de cadastro de pessoas que implementa o padrão MVC. A parte relativa ao Modelo pode ser vista na classe `Modelo` (e suas subclasses) em conjunto com o dicionário `banco_de_dados` que é usado para simular um banco de dados. A classe `Controlador` define o fluxo de execução a partir dos comandos dados pelo usuário (poderia ter sido implementada como uma função, mas foi utilizada a classe evidênciar seu papel) e as visualizações são feitas pela classe `PaginaPrincipal` e suas subclasses.

## Blog da internet (Python)

O padrão MVC é provavelmente o padrão de projeto mais popular para criação de aplicações Web, por isso muitas linguagens de programação possuem diversos _frameworks_ específicos para este fim: Flask e Django no Python, Rails e Sinatra no Ruby, Laravel em PHP e Spring no Java.

Neste exemplo criamos duas versões de um pequena aplicação de blog baseado [neste tutorial](http://turing.com.br/material/flask/tutorial/folders.html) do _framework_ Flask. Flask é um _microframework_ em Python que implementa o padrão MVT (_Model-View-Template_), uma variação do padrã MVC.

Em ambas as versões, no arquivo `flaskr.py` definimos o nosso controlador `app`, onde registramos as nossa rotas, e as visualizações são os arquivos presentes na pasta `templates`. Note que embora os arquivos de template possuam a extensão `.html` eles são arquivos de template da biblioteca `Jinja` da linguagem Python, que cria arquivos que mesclam _tags_ HTML com código python para gerar visualizações dinâmicas.

Na versão 1 o modelo é somente representado na conexão com o banco de dados pela função `conectar_bd` e todas as operações nos dados são realizadas pelo controlador dentro da rota. Na segunda versão do código utilizamos em conjunto com o Flask o _framework_ SQLAlchemy, que provê um mapeamento das classes definidas com o banco de dados, assim o modelo em questão é o _post_ do blog representado pela classe `Post` (que herda suas funcionalidades básicas da classe `bd.Model`).
