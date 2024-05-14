# Escreva um programa em python que leia números inteiros do teclado.

soma = 0
quantidade = 0

while True:
    numero = int(input("digite um numero ou digite 0 para sair : "))
    if numero == 0:
        break

    soma += numero
    quantidade +=1
if quantidade == 0:
    print("obrigado por usar meu programa até breve ")

else:  
    media = soma / quantidade  
    print(f"Quantidade de números digitados: {quantidade}")
    print(f"Soma dos números digitados: {soma}")
    print(f"Média dos números digitados: {media}")


# O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.