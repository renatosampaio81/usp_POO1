# Padrão Estado (_State_)

Códigos com exemplos do padrão Estado (_State_) do livro GoF.

## Conexões de Rede (C++)

Nesse exemplo de código criado por Chris Sharver o padrão Estado é utilizado para para trocar o comportamento da classe que modela uma conexão TCP/IP (`TCPConnection`) de acordo com o estado da conexão: fechada (`TCPClosed`), estabelecida (`TCPEstablished`) e ouvindo (`TCPListen`).

O código completo você encontra no [site do Chris Sharvers](https://www.evl.uic.edu/scharver/labreports/patterns/state.html#Known)

## PyFSM (Python)

O PyFSM é um modulo Python que disponibiliza classes para o desenvolvimento de aplicativos dirigidos a evento. Você pode encontrar a implementação do padrão Estado no arquivo [`state\_machine.py`](https://github.com/jbarbadillo/pyFSM/blob/develop/pyfsmlib/state_machine.py) onde estão declaradas as classes `State` que representa um estado e `StateMachine` a classe contexto que utiliza os diversos estados.

## FiniteStateMachine (Python/DSL)

Outro exemplo de uso do padrão Estado é o software [FiniteStateMachine](https://wiki.python.org/moin/FiniteStateMachine). Esse software permite a criação de uma Linguagem de Domíno Específico (DSL - _Domain Specific Language_) a partir do desenho de um diagrama de estados. O [tutorial](http://fsme.sourceforge.net/doc/tutorial.html) da  documentação oficial do software possui alguns exemplos de utilização do software e da DSL gerada.
