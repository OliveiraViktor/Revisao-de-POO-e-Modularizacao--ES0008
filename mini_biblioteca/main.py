
from src.mini_biblioteca.usuarios import Usuario
from src.mini_biblioteca.emprestimos import Emprestimo
from src.mini_biblioteca.livros import Livro

u1 = Usuario("Ana", "U1")
print(u1.nome)
l1 = Livro("O Hobbit","J.R.R Tolkien","L1",True)

e1 = Emprestimo(l1, u1, True)
e1.criar

print(l1.disponivel)
print(e1.ativo)

e1.devolver
print(e1.ativo)