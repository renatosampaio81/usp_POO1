# Utilizando um dicionario para simular uma banco de dados no Python
# Cada tabela é uma lista associada a chave com o nome da tabela.
banco_de_dados = {}


# Faz a iniciaização do Banco de dados criando uma lista para cada classe
# no modelo
def inicializa_banco():
    global banco_de_dados
    banco_de_dados = {s.__tabela__: [] for s in Modelo.__subclasses__()}


class Modelo:
    """
    Classe Modelo que centraliza os métodos comuns a todos os modelos
    utilizados
    """
    def salvar(self) -> int:
        """
        Salva o objeto no Banco de dados e retorna código gerado gerado
        """
        # caso a entrada não exita no banco
        if not self.id:
            self.id = len(banco_de_dados[self.__tabela__]) + 1
            banco_de_dados[self.__tabela__].append(None)
        banco_de_dados[self.__tabela__][self.id - 1] = self.info()
        return self.id

    @classmethod
    def carregar(cls, id: int):
        """
        Carrega a entrada com o codigo do banco de dados e retorna
        uma instância do Modelo
        """
        dados = banco_de_dados[cls.__tabela__][id - 1]
        pessoa = cls(**dados)
        return pessoa

    @classmethod
    def carregar_todos(cls):
        """
        Retorna uma lista com todos os Modelos cujas entradas estão em
        uma tabela do banco
        """
        pessoas = [cls(**dados) for dados in banco_de_dados[cls.__tabela__]]
        return pessoas


class Pessoa(Modelo):
    """
    Cria o Modelo de uma pessoa, com nome e sobrenome.
    """

    __tabela__ = 'pessoas'

    def __init__(self, nome, sobrenome, cpf, id=None):
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome

    def info(self):
        """
        Método que constrói a representação do Objeto no Banco.
        """
        return {'nome': self.nome, 'sobrenome': self.sobrenome,
                'cpf': self.cpf, 'id': self.id}


class PaginaPrincipal:
    """
    Visualização (View) da página Principal e única
    """
    def __init__(self):
        print("Comandos aceitos:")
        print("    criar_pessoa cpf nome sobrenome")
        print("    mostrar_pessoas")
        print("    mostrar_pessoa id")
        print("    pagina_principal")
        print('    sair')
        print()


class VerPessoas(PaginaPrincipal):
    """
    Visualização das pessoas.
    """
    def __init__(self, pessoas):
        for p in pessoas:
            print(f"{p.id}) {p.cpf} {p.nome} {p.sobrenome}")
        print()
        super().__init__()


class SalvoSucesso(PaginaPrincipal):
    """
    Visualização de salvar com sucesso no banco.
    """
    def __init__(self, id):
        print(f"Pessoa criada com o código: {id}")
        print()
        super().__init__()


class NaoEncontrada(PaginaPrincipal):
    """
    Visualização de dado não encontrado;
    """
    def __init__(self):
        print('Pessoa Não encontrada')
        print()
        super().__init__()


class ComandoDesconhecido(PaginaPrincipal):
    """
    Vizualização de comando desconhecido.
    """
    def __init__(self):
        print('Comando desconhecido!')
        print()
        super().__init__()


class Controlador:
    """
    Classe controlador responsável pelo laço de execução e por interagir
    com o modelo e as visualizações.
    """
    def __init__(self):
        inicializa_banco()
        self.pagina_principal()
        self.laco_principal()

    def laco_principal(self):
        """
        Laço principal do programa: lê o comando do usuário,
        delega a execução do comando para o modelo, e mostra o resultado
        através das visualizações.
        """
        while True:
            comando, *args = input().split()
            try:
                getattr(self, comando)(*args)
            except IndexError:
                NaoEncontrada()
            except AttributeError:
                ComandoDesconhecido()
            except Exception:
                break

    @staticmethod
    def sair():
        """
        Método de saída do programa
        """
        raise Exception

    @staticmethod
    def pagina_principal():
        """
        Carrega a página principal
        """
        PaginaPrincipal()

    @staticmethod
    def mostrar_pessoas():
        """
        Mostra todas as Pessoas do Banco
        """
        pessoas = Pessoa.carregar_todos()
        VerPessoas(pessoas)

    @staticmethod
    def mostrar_pessoa(id):
        """
        Mostra a pessoa que possui o código fornecido
        """
        pessoa = Pessoa.carregar(int(id))
        VerPessoas([pessoa])

    @staticmethod
    def criar_pessoa(cpf, nome, sobrenome):
        """
        Cria uma nova pessoa.
        """
        pessoa = Pessoa(nome, sobrenome, cpf)
        id = pessoa.salvar()
        SalvoSucesso(id)


if __name__ == '__main__':
    Controlador()
