# Padrão Fábrica abstratrata (_Abstract Factory_)

Códigos com exemplos do padrão Fábrica abstrata (_Abstract Factory_) do livro GoF.

## Mudança de tema de jogo (Python)

O arquivo `jogo.py` implementa um jogo com 2 tipos de temas diferentes: Faroeste e Espacial. São definidas as famílias de produtos para cada tema e criadas as fábricas concretas para cada um dos dois temas. Ao executar o script e possível escolher em tempo de execução entre os temas implementados e ver o resultado de um pequeno teste para cada produto da familia.

## Criação de de componentes gráficos (Python)

O Arquivo `gui.py` implementa uma abstração da criação de diferentes componentes gráficos para diferentes sistemas operacionais (GNU/Linux, Windows e MacOS). Nesse exemplo é criada uma classe `FabricaGUI` que no momento de sua instânciação configura quais classes concretas usar para cada componente com base no sistema operacional detectado.

## Uso do Padrão Fábrica Abstrata em Python

Devido ao fato de que na linguagem Python classes e funções são objetos de primeira ordem, isto é, podem ser guardados em vaiáveis, passados como parâmetros e devolvidos como valor de retorno de funções, a implementação de grande parte dos Padrões criacionais pode ser substituida por uso de outros recursos da linguagem. Um exemplo bem conciso é descrito [nesse artigo](https://python-patterns.guide/gang-of-four/abstract-factory/) da página `python-patterns.guide` (em Inglês)