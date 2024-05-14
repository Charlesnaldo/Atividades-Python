# [PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
# Para isso, você deve implementar um módulo que contém as seguintes funções:

alunos = {}

# AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.

def AdicionarAluno():
    nome = input("Digite o seu nome:")
    matricula = input("Digite a MAtricula ")
    alunos[matricula] = nome
    print( " Aluno Adicionado ")

# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
def RemoverAluno():
    matricula = input("digite o numero da matricula do aluno a ser removido")
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno Removido")
    else:
        print("O Aluno não existe no banco de dados.")  

# AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .

def AtualizarAluno(): 
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        alunos[matricula] = novo_nome
        print("Nome do aluno atualizado.")
    else:
        print("Aluno não encontrado.")

# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
def VerAlunos():
    for matricula, nome in alunos.items():
        print("Matrícula:", matricula, " - Nome:", nome)

# Lembre Se de Modularizar o código
while True:
    print("\nSelecione a opção desejada:")
    print("1. Adicionar Aluno")
    print("2. Remover Aluno")
    print("3. Atualizar Aluno")
    print("4. Ver Alunos")
    print("5. Sair agora")

    opcao = input("Opção: ")

    if opcao == "1":
        AdicionarAluno()
    elif opcao == "2":
        RemoverAluno()
    elif opcao == "3":
        AtualizarAluno()
    elif opcao == "4":
        VerAlunos()
    elif opcao == "5":
        print("Até breve.")
        break
    else:
        print("Opção inválida. Tente novamente.")