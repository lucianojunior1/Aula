class Lista:
    def __init__(self):
        self.lista = []

    def inserir(self, dados):
        self.lista.append(dados)


class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, dados):
        self.pilha.append(dados)

    def pop(self):
        return self.pilha.pop()


class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, dados):
        self.fila.append(dados)

    def dequeue(self):
        return self.fila.pop(0)


lista = Lista()
pilha = Pilha()
fila = Fila()

# Passo 1: Inserir os números [1, 2, 3, 4, 5] na lista
for i in range(1, 6):
    lista.inserir(i)

# Passo 2: Remover os dados da lista e inserir na pilha
while len(lista.lista) > 0:
    dado = lista.lista.pop(0)
    pilha.push(dado)

# Passo 3: Remover os dados da pilha e inserir na fila
while len(pilha.pilha) > 0:
    dado = pilha.pop()
    fila.enqueue(dado)

# Passo 4: Inserir os números [6, 7, 8, 9, 10] na lista
for i in range(6, 11):
    lista.inserir(i)

# Passo 5: Repetir os passos 2 e 3
while len(lista.lista) > 0:
    dado = lista.lista.pop(0)
    pilha.push(dado)

while len(pilha.pilha) > 0:
    dado = pilha.pop()
    fila.enqueue(dado)

# Passo 6: Exibir todos os números inseridos na fila
while len(fila.fila) > 0:
    dado = fila.dequeue()
    print(dado)