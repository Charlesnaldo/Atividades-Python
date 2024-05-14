notas = []

for i in range(4):
    nota=int(input("Qual sua nota ?"))
    notas.append(nota)

print(notas)

soma = sum(notas)
quant= len(notas)
media = soma/quant

print(f"a sua média é {media}")


