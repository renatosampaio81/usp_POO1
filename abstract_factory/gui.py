from platform import system


# Familia de produtos para Windows
class BotaoWindows:
    def __init__(self):
        print("Eu sou um botão no Windows")


class JanelaWindows:
    def __init__(self):
        print("Eu sou uma janela no Windows")


# Familia de produtos para Linux
class BotaoLinux:
    def __init__(self):
        print("Eu sou um botão no Linux")


class JanelaLinux:
    def __init__(self):
        print("Eu sou uma janela no Linux")


# Familia de produtos para MacOS
class BotaoMac:
    def __init__(self):
        print("Eu sou um botão no MacOS")


class JanelaMac:
    def __init__(self):
        print("Eu sou uma janela no MacOs")


class FabricaGUI:
    """
    Classe Fábrica que determina o tipo de sistema operacional e seleciona a
    fábrica apropriada
    """
    def __init__(self):
        if system() == "Windows":
            self.fabrica = FabricaWindows()
        elif system() == "Linux":
            self.fabrica = FabricaLinux()
        elif system() == "Darwin":
            self.fabrica = FabricaMacOS()
        else:
            raise TypeError('Sistema Operacional não identificado.')

    def criar_botao(self):
        return self.fabrica.criar_botao()

    def criar_janela(self):
        return self.fabrica.criar_janela()


class FabricaWindows:
    """
    Fabrica de componentes para o Sistema operacional Windows
    """
    def criar_botao(self):
        return BotaoWindows()

    def criar_janela(self):
        return JanelaWindows()


class FabricaLinux:
    """
    Fabrica de componentes para o Sistema operacional Linux
    """
    def criar_botao(self):
        return BotaoLinux()

    def criar_janela(self):
        return JanelaLinux()


class FabricaMacOS:
    """
    Fabrica de componentes para o Sistema operacional MacOs
    """
    def criar_botao(self):
        return BotaoMac()

    def criar_janela(self):
        return JanelaMac()


if __name__ == '__main__':
    fabrica_gui = FabricaGUI()
    fabrica_gui.criar_janela()
    fabrica_gui.criar_botao()
