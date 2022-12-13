# Padrão Adaptador (_Adapter_)

Códigos com exemplos do padrão Adaptador (_Adapter_) do livro GoF.

## Classe Matemática

O arquivo `matemática.py` implementa um exemplo de uso do padrão adaptador para adequar os nome dos métodos presentes no módulo matemática para a interface com o nome das funções modificadas.

## Tartaruga

O Arquivo `tartaruga.py` é o mesmo código presente no exemplo do padrão Estratégia (_Strayegy(85)_), nele podemos notar que cada uma das classes de estratégia são adaptações do método `save` da classe `Image`, onde foram adaptados tanto o nome do método quanto os parâmetros que são passados.

## Carregadores de celular

O arquivo `carregador.py` mostra um código exemplo presente na [página do Wikipédia do padrão Adaptador](https://en.wikipedia.org/wiki/Adapter_pattern). No código são criados dois modelos de telefone celular (Iphone e Android), que usam carregadores dois tipos de conectores diferentes (Lithning e Micro USB) e é criada uma classe para adaptar o uso do padrão Micro USB para o Iphone, delegando o método `usar_micro_usb` par ao método `usar_lightning`. 

## Palestra do Peter Ullrich

Na Python Conference 2017 (PyCon17) na Suécia, o engenheiro de software Peter Ullrich fez uma palestra sobre o uso de padrões de projeto em python ([link para o vídeo](https://www.youtube.com/watch?v=bsyjSW46TDg)). Nessa palestra ele demonstra o uso dos Padrões: Adaptador, Fachada e Observador. O padrão Adaptador é apresentado em 3 versões nos arquivos: [`adapter\_okay.py`](https://github.com/PJUllrich/Design-Patterns/blob/master/adapter_okay.py), [`adapter\_better.py`](https://github.com/PJUllrich/Design-Patterns/blob/master/adapter_better.py) e [`adapter\_best.py`](https://github.com/PJUllrich/Design-Patterns/blob/master/adapter_best.py)