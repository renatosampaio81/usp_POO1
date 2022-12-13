class IPhone:
    __name__ = "iPhone"

    def __init__(self):
        self.conectado = False

    def usar_lightning(self):
        self.conectado = True
        print("Conectado ao carregador lightning")

    def recarregar(self):
        if self.conectado:
            print("Carregando...")
            print("Bateria recarregada.")
        else:
            print("Conecte ao carregador lighning antes")


class Android:
    __name__ = "Android"

    def __init__(self):
        self.conectado = False

    def usar_micro_usb(self):
        self.conectado = True
        print("Conectado ao carregador Micro USB")

    def recarregar(self):
        if self.conectado:
            print("Carregando...")
            print("Bateria recarregada.")
        else:
            print("Conecte ao carregador Micro USB antes")


class AdaptadorIPhone:
    def __init__(self, celular: IPhone):
        self.celular = celular

    def recarregar(self):
        self.celular.recarregar()

    def usar_micro_usb(self):
        print("Conectado ao carregador Micro USB")
        self.celular.usar_lightning()


class CarregadorAndroid:
    def __init__(self):
        self.telefone = Android()
        self.telefone.usar_micro_usb()
        self.telefone.recarregar()


class CarregadorIPhone:
    def __init__(self):
        self.telefone = IPhone()
        self.telefone.usar_lightning()
        self.telefone.recarregar()


class CarregadorIPhoneMicroUSB:
    def __init__(self):
        self.telefone = IPhone()
        self.adaptador_telefone = AdaptadorIPhone(self.telefone)
        self.adaptador_telefone.usar_micro_usb()
        self.adaptador_telefone.recarregar()


if __name__ == '__main__':
    print("Recarregando Android com MicroUSB")
    CarregadorAndroid()
    print()

    print("Recarregando o iPhone com MicroUSB usando o adaptador.")
    CarregadorIPhoneMicroUSB()
    print()

    print("Recarregando o iPhone com Lightning.")
    CarregadorIPhone()
