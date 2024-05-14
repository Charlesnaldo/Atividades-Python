

lista_numeros = []
lista_pares = []
lista_impares =[]

for i in range(10):
    numero = int(input("digite um numero:  "))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)


lista_impares = tuple(lista_impares)

print("Numeros pares são : \n",lista_pares )
print("Numeros impares são : \n",lista_impares)     

# print(type(lista_impares)) para testar se mudou para tuple

print("O total de numeros pares são",len(lista_pares))
print("O total de numeros impares são",len(lista_impares))


soma_pares = sum(lista_pares)
soma_impares = sum(lista_impares)


print(f"Soma dos números pares:{soma_pares} Soma dos números ímpares: {soma_impares}")