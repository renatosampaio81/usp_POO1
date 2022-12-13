# Exemplo do Padrão Estratégia (Strategy) adaptado do livro
# "Head First Design Patterns"
#
# Neste arquivo a implementação segue de maneira parecida a implementação em
# Java do livro Original, o arquivo pato_pythonico.py possui uma versão
# alternativa com mais recursos da linguagem python

class ComportamentoDeVoar:
    """
    Classe "abstrata" para a estratégia de voar, não é realmente
    necessária a criação dessa classe, uma vez que a linguagem python possui
    tipagem fraca, e portanto também não é necessário que as estratégias
    herdem dessa classe. Aqui foi feito assim por motivos didáticos.
    """
    def voar(self):
        raise NotImplementedError


class NaoVoa(ComportamentoDeVoar):
    """
    Classe para a estratégia de não voar.
    """
    def voar(self):
        print("Eu não vôo.")


class VoaComAsas(ComportamentoDeVoar):
    """
    Classe para a estratégia de Voar com asas.
    """
    def voar(self):
        print("Estou Voando!")


class ComportamentoDeGrasnar:
    """
    Classe "abstrata" para a estratégia de grasnar, não é realmente
    necessária a criação dessa classe, uma vez que a linguagem python possui
    tipagem fraca, e portanto também não é necessário que as estratégias
    herdem dessa classe. Aqui foi feito assim por motivos didáticos.
    """
    def grasnar(self):
        raise NotImplementedError


class Grasna(ComportamentoDeGrasnar):
    """
    Classe para a estratégia de grasnar.
    """
    def grasnar(self):
        print("Quack")


class Squeak(ComportamentoDeGrasnar):
    """
    Classe para a estratégia de fazer "squeak".
    """
    def grasnar(self):
        print("Squeak")


class NaoGrasna(ComportamentoDeGrasnar):
    """
    Classe para a estratégia de não grasnar.
    """
    def grasnar(self):
        print("<< Silêncio... >>")


class Pato:
    """
    Esta classe modela os comportamentos comuns a todos os tipos de pato.
    """
    comportamento_de_voar = None
    comportamento_de_grasnar = None

    def __repr__(self):
        raise NotImplementedError

    def voar(self):
        self.comportamento_de_voar.voar()

    def grasnar(self):
        self.comportamento_de_grasnar.grasnar()

    def nadar(self):
        print("Todos os patos boiam, inclusive as iscas")


class PatoReal(Pato):
    """
    Classe que modela um pato real.Patos reais voam e grasnam.
    """
    comportamento_de_grasnar = Grasna()
    comportamento_de_voar = VoaComAsas()

    def __repr__(self):
        return "Eu sou um pato real de verdade"


class PatoBorracha(Pato):
    """
    Classe que modela um pato de borracha. Patos de
    borracha não voam e fazem "squeak", ao invés de
    grasnar
    """
    comportamento_de_grasnar = Squeak()
    comportamento_de_voar = NaoVoa()

    def __repr__(self):
        return "Eu sou um pato de borracha"


def main():
    """
    "Simulador de Patos" do exemplo do livro.
    """
    pato_real = PatoReal()
    print(pato_real)
    pato_real.grasnar()
    pato_real.voar()

    pato_borracha = PatoBorracha()
    print(pato_borracha)
    pato_borracha.grasnar()
    pato_borracha.voar()


if __name__ == '__main__':
    main()
