# Exemplos dos Padrões de Projeto

Neste repositório, estão os exemplos em código referentes ao curso Laboratório de Programação Orientada a Objetos (Partes 1 e 2) ministrado pelo Prof. Dr. Fabio Kon na plataforma Coursera. Os exemplos foram criados por Guilherme Feulo, da equipe de produção dos cursos.

## Padrões

### Arquitetural
* [MVC (_Model-View-Controller_)](mvc)

### Comportamentais
* [Estado (_State_)](state)
* [Estratégia (_Strategy_)](strategy)

### Criacionais
* [Fábrica Abstrata (_Abstract Factory_)](abstract_factoory)
* [Método Fábrica (_Factory Method_)](factory_method)
* [_Singleton_](singleton)

### Estruturais
* [Adaptador (_Adapter_)](adapter)



## Dependências

Os exemplos em linguagem Python necessitam que a versão do Python seja a 3.5 ou mais recente (Python2 não é suportado). O Arquivo `requirements.txt` presente no repositório mantém uma lista dos módulos python necessários para execução dos exemplos. Você pode instalar todas as dependências com o comando:
```
pip install -r requirements.txt
```
A utilização de uma ambiente virtual como o [`virtualenv`](https://virtualenv.pypa.io/en/latest/) é altamente recomendada para evitar conflitos com as versões já presentes na sua instalação do python.

## Guia de instalação do GhostScript para Windows

Se você utiliza Sistema Operacional da Família Windows, para execução dos exemplos que envolvem conversão de imagens (versões de `tartaruga.py`) é necessária a instalação do software [GhostScript](https://www.ghostscript.com), utilizado pela biblioteca de imagens da Linguagem Python.

Faça o download do arquivo de instalação na [página oficial do GhostScript](https://www.ghostscript.com/download/gsdnld.html). Selecione o arquivo para baixae na coluna _GNU Affero General Public License_ de acordo com a aarquitetura do seu sistema (32 ou 64 bits).
Ao concluir o download execute o instalador e surante a execução do _setup_ copie o caminho de instalção do GhostScript (o padrão é C:\\Program Files\\gs\\gs9.53.3\\).

Ao concluir abra o Painel de controle do Windows entre em "Sistema e Segurança" e depois em "Sistema". Em seguida clique em "Configurações avançadas do Sistema" (no lado direito) e em seguida no botão "Variáveis de Ambiente". Na lista "Variáveis do usuário" procure pela variável de nome "Path" e clique em "Editar". Clique no botão "Novo" e cole o caminho de instalação do GhostScript e clique em OK.

Pronto o GhostScript já está instalado e configurado! Se você teve alguma problema durante o processo de inclusão do caminho no _Path_ do sistema você pode dar uma olhada [na página de instalação do Java](https://www.java.com/pt-BR/download/help/path_pt-br.html) também.


## Referências

* Kasampalis, S. (2015). **Mastering Python design patterns**. Packt Publishing Ltd.
* Gamma, E., Helm, R. & Johnson, R., Vlissides, J., (1995). **Design Patterns: Elements of Reusable Object-Oriented Software**. Addison-Wesley Publishing Company.
* Eckel, B. & Friends (acessado em 25/01/2021) **Python3 Patterns, Recipes and Idioms**. disponível em https://python-3-patterns-idioms-test.readthedocs.io/en/latest/index.html

## Outros exemplos em código

* [Refactoring Guru](https://refactoring.guru/design-patterns/)
* [Github sobre padrões de projeto em python](https://github.com/faif/python-patterns)
* [Source Making](https://sourcemaking.com/design_patterns/)
* [python-patterns.guide](https://sourcemaking.com/design_patterns/)

## Palestras

* Alex Martelli on Google TechTalks (2013) [youtube](https://www.youtube.com/watch?v=4KZx8bATBFs) [slides](http://www.aleax.it/goo_pydp.pdf)
* Ariel Ortiz on Pycon Cleveland (2019) [youtube](https://www.youtube.com/watch?v=o1FZ_Bd4DSM) [website](http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html)
* Brandon Rhodes on PyOhio (2012) [youtube](https://www.youtube.com/watch?v=Er5K_nR5lDQ) [slides](https://rhodesmill.org/brandon/slides/2012-07-pyohio/)
* Christopher Neugebauer on PyCon Australia (2018) [youtube](https://www.youtube.com/watch?v=imW-trt0i9I)
* Peter Ullrih on PyCon Suécia (2017) [youtube](https://www.youtube.com/watch?v=bsyjSW46TDg) [github](https://github.com/PJUllrich/Design-Patterns)
* Sebastian Buczyńsk on EuroPython (2017) [youtube](https://www.youtube.com/watch?v=G5OeYHCJuv0)
