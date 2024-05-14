# Escreva um programa em python que pergunte ao usuário a velocidade de um carro

velocidade = float(input("Qual a velocidade do carro em km/h  ? "))



if velocidade > 80:

    kmquepassou = velocidade - 80

    multa = kmquepassou * 20

    print(f"O usuario foi multado em R$ {multa}")
else:
    print( "dentro da velocidade permitida")

# . Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.