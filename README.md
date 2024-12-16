<h1 align="center" style="font-weight: bold;">📚 Sistema de Gerenciamento de Biblioteca 💻</h1> 
<p align="center"> 
    <a href="#desc">Descrição</a> • 
    <a href="#features">Funcionalidades</a> • 
    <a href="#install">Instalação</a> • 
    <a href="#usage">Como Usar</a> • 
    <a href="#data">Estrutura de Dados</a> • 
    <a href="#code">Estrutura do Código</a> 
</p> 
<h2 id="desc" style="font-weight: bold; font-size: 2rem">Descrição</h2>
Este projeto implementa um sistema de gerenciamento de biblioteca em Python. Ele utiliza estruturas de dados avançadas, como árvores AVL, filas circulares e pilhas, para gerenciar livros, reservas e histórico de operações. A aplicação inclui funcionalidades como adição de livros, busca eficiente, empréstimos e devoluções, e desfazer última ação, proporcionando um gerenciamento prático e eficaz.

<h2 id="features" style="font-weight: bold; font-size: 2rem">⚙ Funcionalidades</h2>

- Adicionar Livros: Insere novos livros na biblioteca organizados por uma árvore AVL para buscas rápidas.
- Buscar Livros: Localiza livros pelo título, garantindo eficiência na pesquisa.
- Emprestar Livros: Registra a retirada de livros utilizando uma fila circular para controlar reservas.
- Devolver Livros: Processa a devolução de livros à biblioteca.
- Desfazer Última Ação: Reverte a última operação realizada (empréstimo ou devolução).
- Listar Livros: Exibe todos os livros em ordem alfabética pelo título.

<h2 id="install" style="font-weight: bold; font-size: 2rem">📦 Instalação</h2>

1. Clone este repositório:

```bash
git clone https://github.com/kaychenderson/Python_Library.git
``` 

2. Acesse o diretório do projeto:

```bash
cd Python_Library
``` 

3. Execute o sistema:

Basta rodar o arquivo principal para iniciar o programa:

```bash
python library.py
```

<h2 id="usage" style="font-weight: bold; font-size: 2rem">💡 Como Usar</h2>

- Adicionar Livros: Use o método add_book(codigo, titulo, autor) para cadastrar livros na biblioteca.
Exemplo:
```bash
library.add_book(1, "Dom Casmurro", "Machado de Assis")
```
- Buscar Livros: Use o método search_book(titulo) para localizar um livro pelo título.
Exemplo:
```bash
library.search_book("Dom Casmurro")
```
- Empréstimo de Livros: Utilize borrow_book(titulo) para emprestar um livro.
Exemplo:
```bash
library.borrow_book("Dom Casmurro")
```
- Devolução de Livros: Use return_book() para devolver um livro da fila de reservas.
Exemplo:
```bash
library.return_book("Dom Casmurro")
```
- Desfazer Ações: Utilize undo_last_action() para reverter a última operação de empréstimo ou devolução.

<h2 id="data" style="font-weight: bold; font-size: 2rem">💾 Estrutura de Dados</h2>

O sistema usa diferentes estruturas para oferecer eficiência e organização:

- Árvore AVL: Armazena e organiza livros por título, garantindo buscas rápidas e ordenação automática.
- Fila Circular: Gerencia a fila de reservas de livros.
- Pilha: Armazena o histórico de ações (empréstimos e devoluções), permitindo desfazer operações.

<h2 id="code" style="font-weight: bold; font-size: 2rem">🛠 Estrutura do Código</h2>

O sistema é dividido em classes principais:

- Classe NodeAVL:
Representa cada nó da árvore AVL, armazenando os dados do livro e os ponteiros para os filhos.
- Classe AVLTree:
Implementa a árvore AVL, incluindo métodos para rotação, cálculo de balanceamento e inserção de nós.
- Classe CircularQueue:
Implementa uma fila circular para gerenciar a ordem de reservas.
- Classe Stack:
Fornece uma pilha para armazenar o histórico de ações realizadas.
- Classe Book:
Representa os atributos básicos de um livro, como código, título e autor.
- Classe Library:
Controla a lógica principal, incluindo gestão de livros, empréstimos, devoluções e histórico.