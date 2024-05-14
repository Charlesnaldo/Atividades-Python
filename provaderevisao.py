from functools import reduce

lista_produtos = []

# Função para adicionar um produto à lista
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = float(input("Digite a quantidade do produto: "))  # Alteração aqui
    valor_unitario = float(input("Digite o valor unitário do produto sem virgula: "))
    total = quantidade * valor_unitario
    lista_produtos.append({"produto": nome, "valor": valor_unitario, "quantidade": quantidade, "total": total})
    print("Produto adicionado com sucesso!")

# Função para mostrar a lista de produtos
def mostrar_lista():
    if not lista_produtos:
        print("Lista de produtos vazia.")
    else:
        print("Lista de produtos:")
        for produto in lista_produtos:
            print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor unitário: {produto['valor']}, Total: {produto['total']}")
        calcular_total()

# Função para atualizar informações de um produto
def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in lista_produtos:
        if produto['produto'] == nome:
            quantidade = float(input("Digite a nova quantidade do produto: "))  # Alteração aqui
            valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            produto['quantidade'] = quantidade
            produto['valor'] = valor_unitario
            produto['total'] = quantidade * valor_unitario
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")

# Função para remover um produto da lista
def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in lista_produtos:
        if produto['produto'] == nome:
            lista_produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

# Função para calcular o valor total de todos os produtos da lista
def calcular_total():
    total = reduce(lambda x, y: x + y['total'], lista_produtos, 0)
    print(f"Valor total de todos os produtos: {total}")

# Função principal do programa
def main():
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar produto")
        print("2. Ver lista de produtos")
        print("3. Atualizar produto")
        print("4. Remover produto")
        print("5. Encerrar programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            mostrar_lista()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()