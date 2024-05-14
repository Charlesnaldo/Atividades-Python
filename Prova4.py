# Desenvolva um programa em Python que permita ao usuário digitar várias notas. 

notas = []

for i in range(4):
    nota_aluno = int(input("Digite sua nota: "))
    notas.append(nota_aluno)


# Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno.

def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.

def verificar_situacao(media):
    if media < 7:
        print("Reprovado")
    elif media >= 7 and media <10:
        print("Aprovado")
    elif media == 10:
        print("Parabens, Sua media é 10")    


media_notas = calcular_media(notas)
verificar_situacao(media_notas)
