

alunos = {}

while True:
    print("Menu:")
    print("1. Incluir aluno")
    print("2. tirar aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair agora")

    opcao = input("Escolha uma opção:  ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

    elif opcao == "2":
        matricula = input("Digite o número de matrícula do aluno a ser removido: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Aluno removido com sucesso!")
        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        print("\nLista de alunos:")
        for matricula, nome in alunos.items():
            print(f"Nome: {nome}, Matrícula: {matricula}")

    elif opcao == "4":
        print("Saindo do programa...em 3 2 1 ......... volte sempre!")
        break

    else:
        print("Ei Maxoréi.. só tem de 1 a 4 , se digitar outro numero nao vai funcionar, tenta novamente.")