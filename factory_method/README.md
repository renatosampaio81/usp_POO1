# Padrão Método Fábrica (_Factory Method_)

Exemplos do Padrão Método Fábrica (_Factory Method_) do livro GoF.

## Classes ou tipos Python

Em python classes ou tipos, são objetos de primeira ordem que podem ser chamados e retornam uma instância assim todos os tipos básicos (`int`, `str`) e demais classes da biblioteca padrão do Python (`list`, `dict`) podem ser pensados como fábricas.

## Tartaruga (Python)

No exemplo do arquivo `tartaruga.py` que utilizamos nos Padrões Estratégia e Adaptador, tínhamos um dicionário do python `ESTRATEGIAS_SALVAMENTO` que era responsável por fornecer a  estratégia correta para salvar o arquivo. Esse dicionário combinado com a linha que faz a instanciação do objeto podem ser interpretados como um funcionamento do padrão Método Fábrica. No arquivo `tartaruga.py` a funcionalidade foi colocada dentro de uma função (método) de nome `seleciona_estratégia` para explicitar o uso do padrão.

O arquivo `tartaruga2.py` mostra uma alternativa de implementação onde o método `seleciona_estrategia` é colocado dentro da classe `FabricaEstrategia`, que inicializa a coleção de estratégias possíveis em sua criação. Esta estratégia simplifica o processo de criação de novas estratégias que são automaticamente incluídas na fábrica se forem subclasses de `SalvaTela`.
