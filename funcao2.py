
notas = []

for i in range(3):
    nota=int(input("digite sua nota aqui : "))
    notas.append(nota)
print(notas)    


def calcular_media():
    total = sum(notas)
    media = total/len(notas)
    return media

mediadoaluno = calcular_media()

print(f"Sua media é {mediadoaluno}")