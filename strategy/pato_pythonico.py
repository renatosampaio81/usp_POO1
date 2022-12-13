# Exemplo do Padrão Estratégia (Strategy) adaptado do livro
# "Head First Design Patterns"
#
# Neste arquivo a fazemos uma implementação mais "pythonica" do exemplo
# do livro e do vídeo. Como a linguagem Python permite Herança múltipla,
# ao invés de colocarmos as estratégias como atributos nas classes de contexto,
# podemos incluir todos os métodos desejados na classe de contexto herdando de
# várias classe ao mesmo tempo. Classes que possuem apenas 1 método (ou poucos)
# com o objetivo de injetar funcionalidades em outras classes são chamadas
# de classes Mix-in.

class NaoVoa:
    def voar(self):
        print("Eu não vôo.")


class VoarComAsas:
    def voar(self):
        print("Estou Voando!")


class Grasnar:
    def grasnar(self):
        print("Quack")


class Squeak:
    def grasnar(self):
        print("Squeak")


class GrasnarMudo:
    def grasnar(self):
        print("<< Silêncio... >>")


class Pato:
    """
    Esta classe modela os comportamentos comuns a todos os tipos de pato.
    """
    def __repr__(self):
        raise NotImplementedError

    def nadar(self):
        print("Todos os patos boiam, inclusive as iscas")


class PatoReal(Pato, Grasnar, VoarComAsas):
    """
    Classe que modela um pato real.Patos reais voam e grasnam.
    """
    def __repr__(self):
        return "Eu sou um pato real de verdade"


class PatoBorracha(Pato, Squeak, NaoVoa):
    """
    Classe que modela um pato de borracha. Patos de
    borracha não voam e fazem "squeak", ao invés de
    grasnar
    """
    def __repr__(self):
        return "Eu sou um pato de borracha"


if __name__ == '__main__':
    pato_real = PatoReal()
    print(pato_real)
    pato_real.grasnar()
    pato_real.voar()

    pato_borracha = PatoBorracha()
    print(pato_borracha)
    pato_borracha.grasnar()
    pato_borracha.voar()
