from copy import deepcopy
from time import sleep, time


# Familia de Produtos do tema Faroeste
class Cavalo:
    def __init__(self):
        sleep(1)  # simula uma computação complexa para a criação do objeto

    def movimentar(self):
        print("Pocotó, Pocotó, Pocotó...")


class Cauboi:
    def __init__(self):
        sleep(1.5)  # simula uma computação complexa para a criação do objeto

    def falar(self):
        print('Irráaa')


class Revolver:
    def __init__(self):
        sleep(0.25)  # simula uma computação complexa para a criação do objeto

    def atirar(self):
        print('Pow!')


class Faroeste:
    def __init__(self):
        self.itens = {
            'cavalo': Cavalo(),
            'cauboi': Cauboi(),
            'arma': Revolver()
        }

    def criar(self, item):
        return deepcopy(self.itens[item])


if __name__ == '__main__':
    # Iniciliza o Jogo com o cenario escolhido
    print("Iniciando a Fabrica de elementos:", end=' ')
    start = time()
    cenario = Faroeste()
    print(f'Levou {time() - start:.2f} segundos')

    print('Criando um Cauboi')
    start = time()
    cauboi1 = cenario.criar('cauboi')
    print(f'Levou {time() - start} segundos')

    print('Criando outro Cauboi')
    start = time()
    cauboi2 = cenario.criar('cauboi')
    print(f'Levou {time() - start} segundos')
    print('Modificando os caubóis para ver que são instâncias diferentes')
    cauboi1.nome = 'Mau'
    cauboi2.nome = 'Feio'
    print(f'O caubói 1 chama: {cauboi1.nome} e o caubói 2: {cauboi2.nome}.')
