# Utilizando o aprendizado desta aula, implementaremos um sistema de cadastro de senha e inicialização do celular utilizando o loop "for".

senha = "123456"

for tente in range(3,0,-1):
    senhausuario = input(" Digite sua senha: ")

    if senhausuario == senha:
        print(" Bem Vindo !!!" )
        break
    else:
        if tente > 1:
            print(f'Senha errada, voce tem {tente} tentativas')
        else:
            print("senha incorreta celular bloqueado") 


# Após ligar o celular, o usuário é solicitado a inserir a senha cadastrada.
# São permitidas 3 tentativas até que o telefone seja bloqueado.
# Se o usuário acertar a senha, uma mensagem de boas-vindas é exibida: "Bem-vindo."
# Se o usuário errar a senha, uma mensagem informando o erro é exibida, junto com o número de tentativas restantes até o bloqueio do telefone.
# Pense em todas as possibilidades e faça um sistema completo