# Padrão Método Fábrica (_Factory Method_)

Exemplos do padrão de projeto Protótipo (_Prototype_) do livro GoF.

## O módulo `copy` em Python

A biblioteca padrão da linguagem python possui um módulo chamado `copy` que possui funções que permitem a cópia de objetos: `copy(x)` e `deepcopy(x)`. A principal diferença entre essas duas funções é que a função `copy(x)` faz uma cópia "superficial" do objeto `x`, ou seja, ela cópia o objeto `x`, mas todos os objetos a que `x` tem uma referência não são copiados, ao invés disso somente são guardadas referências para estes objetos. A função `deepcopy(x)` por sua vez copia o objeto `x` e faz cópias (de maneira recursiva) de todos os objetos para que `x` faz referência, o que é chamado de cópia profunda.

Para saber mais sobre o módulo `copy` você pode dar uma olhada em sua [documentação oficial](https://docs.python.org/3/library/copy.html).

## Jogo de Faroeste

O arquivo `jogo.py` é baseado no exemplo de mesmo nome do padrão fábrica abstrata, mas foi simplificado e contém apenas o tema de Faroeste. A criação direta de instâncias das classes `Arma`, `Cauboi` e `Cavalo` é artificialmente implementada para simular uma criação de objeto complexo. A classe `Faroeste` por sua vez inicializa um objeto de cada tipo, e ao chamarmos o seu método criar ela devolve uma cópia da instância da classe requisitada, economizando o tempo de processamento envolvido na criação.

## Biblioteca Music21

A biblioteca [Music21](http://web.mit.edu/music21/) é um conjunto de ferramentas desenvolvida para análise musicológica auxiliada por computador. A criação de cópias de objetos como partituras, notas e alturas é realizada durante a chamada de métodos que fazem alterações no conteúdo original para preservar seu estado. Você pode ver alguns exemplos aqui: [cópia do objeto `Score`](https://github.com/cuthbertLab/music21/blob/747316f350319f0832d704c5d06a0c0bc2f07cbe/music21/variant.py#L232), [cópia do objeto `Chord`](https://github.com/cuthbertLab/music21/blob/526bd3cea57aefaa855080d8870aa33bcf9f1ce4/music21/analysis/neoRiemannian.py#L35).

## Visualization ToolKit (VTK)

Outro exemplo de software que implementa o padrão Protótipo (_Prototype(xxx)_) é o [VTK](https://vtk.org/) um conjunto de ferramentas para visualização e criação de imagens 3D. A criação de diversos elementos gráficos é feita através do método `newInstance` (que devolve uma instância prototítica _Singleton_) em conjunto com o método `DeepCopy` que copia os atributos de outra instância usada como base. [Aqui](https://github.com/Kitware/VTK/blob/8526db81234971bb2a36f12ee322b1b277841303/Rendering/Core/Testing/Python/cells.py#L62) você consegue ver que a instância `aVoxel` é criada e inicializada de maneira natural e na sequência a instância `bVoxel` é feita a partir do protótipo e `aVoxel`.

<https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_prototype.htm>

<https://medium.com/design-patterns-in-python/prototype-design-pattern-in-python-45f8d3f15583>

<https://refactoring.guru/design-patterns/prototype/python/example>