# Função para testar se uma variável armazena uma classe
from inspect import isclass


class Tabuleiro:
    """
    Classe que modela um tabuleiro em um jogo de xadrez.
    """
    _instancia = None

    # Método __new__ alterado para somente criar uma instância da classe
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = object.__new__(cls)
        return cls._instancia


if __name__ == '__main__':
    t1 = Tabuleiro()
    t2 = Tabuleiro()
    print(f'As variáveis t1 e t2 referenciam o mesmo objeto: {t1 is t2}')
    print(f'A classe de t1 é: {type(t1)}')
    print(f'Tabuleiro é classe: {isclass(Tabuleiro)}')
