class NodeAVL:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T = x.right
        x.right = y
        y.left = T
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left
        y.left = x
        x.right = T
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key, value):
        if not root:
            return NodeAVL(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"{root.key}: {root.value}")
            self.inorder_traversal(root.right)

class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.max_size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.max_size == self.front:
            print("Fila cheia")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Fila vazia")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return data

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def peek(self):
        return self.stack[-1] if self.stack else None

class Book:
    def __init__(self, code, title, author):
        self.code = code
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.code}: {self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books_tree = None
        self.avl = AVLTree()
        self.reservation_queue = CircularQueue(5)
        self.history_stack = Stack()

    def add_book(self, code, title, author):
        book = Book(code, title, author)
        self.books_tree = self.avl.insert(self.books_tree, title, book)
        print(f"Livro adicionado: {book}")

    def search_book(self, title):
        current = self.books_tree
        while current:
            if title == current.key:
                print(f"Livro encontrado: {current.value}")
                return current.value
            elif title < current.key:
                current = current.left
            else:
                current = current.right
        print("Livro não encontrado")
        return None

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            self.reservation_queue.enqueue(book)
            self.history_stack.push(("borrow", book))
            print(f"Livro emprestado: {book}")

    def return_book(self):
        book = self.reservation_queue.dequeue()
        if book:
            self.history_stack.push(("return", book))
            print(f"Livro devolvido: {book}")

    def undo_last_action(self):
        action = self.history_stack.pop()
        if not action:
            print("Nenhuma ação para desfazer")
            return
        action_type, book = action
        if action_type == "borrow":
            self.reservation_queue.dequeue()
            print(f"Desfazer empréstimo: {book}")
        elif action_type == "return":
            self.reservation_queue.enqueue(book)
            print(f"Desfazer devolução: {book}")

    def display_books(self):
        print("Livros na biblioteca:")
        self.avl.inorder_traversal(self.books_tree)

library = Library()
library.add_book(1, "The Catcher in the Rye", "J.D. Salinger")
library.add_book(2, "To Kill a Mockingbird", "Harper Lee")
library.add_book(3, "1984", "George Orwell")
library.display_books()
library.borrow_book("1984")
library.return_book()
library.undo_last_action()