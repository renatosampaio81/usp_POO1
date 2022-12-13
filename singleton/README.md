# Padrão Singleton

Códigos com exemplos do padrão _Singleton_ do livro GoF.

## Sobre o uso (e implementação) do Padrão _Singleton_ em Python

Por não ser possível implementar atributos e métodos privados em Python (inclusive construtores), existem diferentes estratégias para implementação do padrão _Singleton_. Você pode econtrar as principais estratégias neste [tópico do StackOverflow](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python) onde é explicado em detalhe cada variante e suas respectivas vantanges e desvantagens.

Nos exemplos a seguir utilizamos a implementação que altera o funcionamento do método `__new__` em python, responsável pela de criação dos objetos da sua classe, retornando sempre o mesmo objeto.
Para entender o fluxo de execução dos exemplos em código é necessário entender as diferenças entre os métodos `__init__` e `__new__` da linguagem Python que você pode ler [neste tópico do StackOverflow](https://pt.stackoverflow.com/questions/177882/qual-%C3%A9-a-diferen%C3%A7a-entre-init-e-new).

## Software de computação gráfica (Python)

Um exemplo de utilização dessa implementação do padrão _Singleton_ com instânciação tardia pode ser encontrada na classe [`Shaders`](https://github.com/mjck/mac420/blob/d8c29be0be461144b93ef94d6cd289208bbc3bdf/Source/Graphics/Shaders.py#L5) do repositório de códigos da disciplina MAC-420 Introdução à Computação Gráfica disponibilizado pelo professor Marcel Jackowski (IME-USP).

## Tabuleiro de Xadrez (Python)

O arquivo `xadrez.py` mostra o a implementação desse método corrigindo o problema da classe do objeto devolvido (que no exemplo anterior é diferente da declarada), para a criação de um tabuleiro de xadrez (exemplo do vídeo)