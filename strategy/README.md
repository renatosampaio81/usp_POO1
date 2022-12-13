# Padrão Estratégia (_Strategy_)

Códigos com exemplos do padrão Estratégia (_Strategy_) do livro GoF.

## Exemplos

### Tartaruga (Python)

Código que gera uma tela (_Canvas_) interativo do módulo `turtle` do Python e utiliza diferentes estratégias para salvar os desenhos feitos com diferentes formatos de arquivo.

Utilize as setas do teclado para movimentar a tartaruga e aperte a teclas `s` para abrir o menu para salvar o arquivo

Para a execução deste código é necessária a instalação do módulo `Pillow`, através do comando `pip install pillow`. Não é necessário fazer esse passo caso você já tenha instalado as dependências do projeto através do comando `pip install -r requirements.txt`

**Nota**: Para o funcionamento deste exemplo no Windows é necessária a instalação do software `ghostscript`. As instruções para instalação e configuração podem ser encontradas [aqui](https://gitlab.com/ccsl-usp/LabPOO/#guia-de-instala%C3%A7%C3%A3o-do-ghostscript-para-windows)

### Simulador de Patos (Python)

Exemplo adaptado do livro "_Head First Design Patterns_"(HFDP). O Arquivo `pato.py` possui uma implementação que é mais próxima da implementação original do livro (em linguagem Java) e o arquivo `pato_pythonico.py` faz uma implementação utilizando recursos presentes na linguagem python que não estão presentes na linguagem Java (Herança múltipla)

### SQLAlchemy (Python)

Um exemplo e software real em python que implementa o padrão estratégia é o módulo SQLAlchemy. O SQLAlchemy é um conjunto de ferramentas SQL e _Object Relational Mapper_(ORM). Seu principal uso é ser uma camada intermediária entre a aplicação em linguagem python e o banco de dados SQL utilizado.

O SQLAlchemy é um software livre e de código aberto mantido por uma grande comunidade, você pode conhecer mais acessando a [página do projeto](https://www.sqlalchemy.org/) e ver o código fonte em seu [GitHub](https://github.com/sqlalchemy/sqlalchemy). Por se tratar de um software com grande complexidade, o código é  bastante extenso e igualmente complexo, para facilitar a visualização abaixo seguem alguns exemplos de utilização do padrão estratégia no código-fonte (com links para as classes)

O uso do padrão estratégia pode ser notado na implementação da classe[`StrategizedProperty`](https://github.com/sqlalchemy/sqlalchemy/blob/575b6dded9a25fca693f0aa7f6d7c6e735490460/lib/sqlalchemy/orm/interfaces.py#L546) que modela propriedades que podem ser estrategizadas (contextos). Um exemplo de propriedade desse tipo são as colunas do banco de dados, modeladas na classe [`ColumnProperty`](https://github.com/sqlalchemy/sqlalchemy/blob/58dc9c00133e13e5690e686e680b8275f162aded/lib/sqlalchemy/orm/properties.py#L40), subclasse de `StrategizedProperty`.

A classe [`LoaderStrategy`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/interfaces.py#L827) é usada como base para as classes de estratégia de carregamento de dados. Assim as estratégias [`ColumnLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L175), [`UninstrumentedColumnLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L130),
[`ExpressionColumnLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L261),[`DeferredColumnLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L344), [`AbstractRelationshipLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L531) e [`DoNothingLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L546) podem ser utilizadas com a classe de contexto `ColumnProperty`.
