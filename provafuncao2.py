
from functools import reduce


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:
# Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
quadrados = list(map(lambda x: x ** 2, numeros))

# Função filter() para obter uma nova lista com números pares da lista numeros
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Função reduce()  para obter a soma de todos os números da lista numeros
soma = reduce(lambda x, y: x + y, numeros)


# aqui o resultado obitido
print("Quadrados dos números:", quadrados)
print("Números pares:", pares)
print("Soma de todos os números:", soma)