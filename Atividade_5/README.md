# Atividade 5

## 1. Parâmetros do Makefile

Tanto `root-config --cflags` quanto `root-config --libs` servem para compilar e linkar o programa:

* **`root-config --cflags`:** Fornece as informações para o compilador (*compiler flags*), a partir do script nativo do root (`root-config`) retornando as opções de compilação e os caminhos dos cabeçalhos do ROOT.
* **`root-config --libs`:** Retorna os caminhos e as bibliotecas compiladas (*linker flags*) necessárias para gerar o executável final.

Essas informações são necessárias, pois o compilador `g++` é genérico e não reconhece a estrutura do ROOT por padrão. Isso é diferente do interpretador do ROOT (CINT/Cling), que já roda com todas essas bibliotecas e caminhos carregados nativamente na memória.

---

## 2. Interface PyROOT e C++

O PyROOT funciona como um tradutor (interface) entre o Python e as bibliotecas nativas do ROOT em C++. O Python não reimplementa as funcionalidades do ROOT, em vez disso, o PyROOT carrega as bibliotecas já compiladas do ROOT no computador e repassa as chamadas diretamente para o C++. Assim o Python funciona apenas como um tradutor de sintaxe simplificada para o C++.

---

## 3. Comparação entre versões

* **Velocidade de Escrita e Execução:** A versão em *PyROOT foi mais rápida de escrever*, devido à sintaxe simplificada e limpa da linguagem, por não precisar declarar explicitamente o tipo dos objetos e por conseguir rodar sem a configuração de um Makefile. Entretanto, a versão em *C++ compilado é a mais rápida para execução*, pois o código é traduzido diretamente para linguagem de máquina com otimizações nativas.

* **Mudanças na Estrutura:** 
  * *Macro para C++ Compilado:* Foi preciso transformar o script solto anterior em um programa real e que virará executável adicionando `int main()`, sendo necessário incluir explicitamente os cabeçalhos (`#include <TTree.h>`, etc) e criar um `Makefile` para ligar as bibliotecas do ROOT.
  * *C++ Compilado para PyROOT:* Além da troca de sintaxes (`->` por `.`), teve mudança direta no gerenciamento de memória. Como o python não possui ponteiros nativos, foi preciso importar a biblioteca `numpy` e criar um array para "simular" o endereço de memória `&x` para utilizar o método `t.Branch`.

* **Checagem de Erros de Tipagem:** A versão em *C++ compilado* é a única que pega erros *antes de rodar*, pois como é uma linguagem fortemente tipada, o compilador `g++` checa todo o código antes de gerar o executável (tempo de compilação). Caso houver algum erro, ele nem chega a gerar este executável. Para a versão em *PyROOT* e *Macro interpretada*, os erros são pegos em *tempo de execução*, ou seja, o script chega a rodar e só apresenta erro no momento em que a linha com o tipo errado é executada. Isso acontece, pois ambas versões rodam através de interpretadores.