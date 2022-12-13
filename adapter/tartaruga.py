from turtle import Turtle, Screen
from PIL import Image
from io import BytesIO
from tkinter import filedialog


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
        """
        Método que faz as adaptações necessárias para a utilização do método
        save da classe Image
        """
        imagem = BytesIO(tela.postscript(colormode='color').encode('utf-8'))
        # Adaptação para o método save da classe Image
        Image.open(imagem).save(nome_arquivo, 'png')


class SalvaTelaPDF(SalvaTela):
    """
    Estratégia para arquivos PDF
    """

    def salvar(self, nome_arquivo: str, tela: Screen):
        """
        Método que faz as adaptações necessárias para a utilização do método
        save da classe Image
        """
        imagem = BytesIO(tela.postscript(colormode='color').encode('utf-8'))
        # Adaptação para o método save da classe Image
        Image.open(imagem).save(nome_arquivo, 'pdf')


class SalvaTelaJPG(SalvaTela):
    """
    Estratégia para arquivos JPG
    """
    def salvar(self, nome_arquivo: str, tela: Screen):
        """
        Método que faz as adaptações necessárias para a utilização do método
        save da classe Image
        """
        imagem = BytesIO(tela.postscript(colormode='color').encode('utf-8'))
        # Adaptação para o método save da classe Image
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

# dicionario que devolve a classe da estratégia adequada
# de acordo com a tipo de arquivo escolhido
ESTRATEGIAS = {
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
        formato = nome_arquivo[-3:]
        salvador = ESTRATEGIAS.get(formato)()
        salvador.salvar(nome_arquivo, self.tela.getcanvas())


if __name__ == '__main__':
    Tartaruga()
