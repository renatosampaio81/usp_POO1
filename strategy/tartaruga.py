from turtle import Turtle, Screen
from PIL import Image
from io import BytesIO
from tkinter import filedialog

# Exemplo de utilização do Padrão Estratégia (Strategy)
#
# Aqui temos como contexto a classe Tartaruga, que utiliza a classe Turtle do
# Python para criar uma tela onde é possível desenhar com o movimento da
# tartaruga, e diferentes estratégias para salvar a tela (cada estratégia gera
# um tipo de arquivo diferente)
#
# Teclas para utilização:
# Seta para cima: movimenta a tartaruga para a frente
# Seta para baixo: movimenta a tartaruga para trás
# Seta para a esquerda: gira a tataruga 45º no sentido anti-horário
# Seta para a direita: gira a tartaruga 45º no sentido horário
# Letra S: abre o menu para salvar a imagem.


class SalvaTela:
    """
    Classe "abstrata" para a estratégia de salvamento, não é realmente
    necessária a criação dessa classe, uma vez que a linguagem python possui
    tipagem fraca, e portanto também não é necessário que as estratégias
    herdem dessa classe. Aqui foi feito assim por motivos didáticos.
    """
    def salvar(self, nome_arquivo, tela):
        raise NotImplementedError


class SalvaTelaPNG(SalvaTela):
    """
    Estratégia para arquivos PNG
    """
    def salvar(self, nome_arquivo: str, tela: Screen):
        imagem = BytesIO(tela.postscript(colormode='color').encode('utf-8'))
        Image.open(imagem).save(nome_arquivo, 'png')


class SalvaTelaPDF(SalvaTela):
    """
    Estratégia para arquivos PDF
    """
    def salvar(self, nome_arquivo: str, tela: Screen):
        imagem = BytesIO(tela.postscript(colormode='color').encode('utf-8'))
        Image.open(imagem).save(nome_arquivo, 'pdf')


class SalvaTelaJPG(SalvaTela):
    """
    Estratégia para arquivos JPG
    """
    def salvar(self, nome_arquivo: str, tela: Screen):
        imagem = BytesIO(tela.postscript(colormode='color').encode('utf-8'))
        Image.open(imagem).save(nome_arquivo, 'jpeg')


class SalvaTelaEPS(SalvaTela):
    """
    Estratégia para arquivos postscript
    """
    def salvar(self, nome_arquivo: str, tela: Screen):
        tela.postscript(colormode='color', file=nome_arquivo)


# lista de tipos aceitos passada como parâmetro
TIPOS = (
    ('Documento PDF', '*.pdf'),
    ('Imagem JPG', '*.jpg'),
    ('Imagem PNG', '*.png'),
    ('Arquivo PostScript', '*.eps')
)

# dicionário que devolve a classe da estratégia adequada
# de acordo com a tipo de arquivo escolhido
ESTRATEGIAS_SALVAMENTO = {
    'pdf': SalvaTelaPDF,
    'jpg': SalvaTelaJPG,
    'png': SalvaTelaPNG,
    'eps': SalvaTelaEPS
   }


class Tartaruga():
    """
    Classe Tartaruga

    Classe responsável por gerar a interface gráfica interativa para o desenho
    e salvá-lo em arquivo de acordo com as diferentes estratégias
    """

    def __init__(self, largura: int = 500, altura: int = 500):
        tartaruga = Turtle('turtle')
        self.tela = Screen()
        self.tela.setup(largura, altura)
        self.tela.onkey(lambda: tartaruga.forward(45), "Up")
        self.tela.onkey(lambda: tartaruga.left(45), "Left")
        self.tela.onkey(lambda: tartaruga.right(45), "Right")
        self.tela.onkey(lambda: tartaruga.back(45), "Down")
        self.tela.onkey(self.salvar, 's')
        self.tela.listen()
        self.tela.mainloop()

    def salvar(self):
        """
        Salva a tela onde foi realizado o desenho de acordo com o formato de
        arquivo escolhido
        """
        nome_arquivo = filedialog.asksaveasfilename(filetypes=TIPOS,
                                                    defaultextension='*.*')
        salvador = ESTRATEGIAS_SALVAMENTO.get(nome_arquivo[-3:])()
        salvador.salvar(nome_arquivo, self.tela.getcanvas())


if __name__ == '__main__':
    Tartaruga()
