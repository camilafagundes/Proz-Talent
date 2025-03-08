class ControleEstoque:
    def __init__(self):
        self.produtos = ["Arroz", "Feijão", "Macarrão", "Óleo", "Açúcar"]

    def listar_produtos(self):
        print("Produtos disponíveis:")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto}")

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto}' adicionado ao estoque.")

    def alterar_produto(self, indice, novo_produto):
        if 0 <= indice < len(self.produtos):
            produto_antigo = self.produtos[indice]
            self.produtos[indice] = novo_produto
            print(f"Produto '{produto_antigo}' substituído por '{novo_produto}'.")
        else:
            print("Índice inválido. Nenhuma alteração feita.")

    def executar(self):
        while True:
            print("\nEscolha uma opção:")
            print("1. Listar produtos")
            print("2. Adicionar produto")
            print("3. Alterar produto")
            print("4. Sair")

            opcao = input("Digite o número da opção desejada: ")

            if opcao == "1":
                self.listar_produtos()
            elif opcao == "2":
                produto = input("Digite o nome do produto a ser adicionado: ")
                self.adicionar_produto(produto)
            elif opcao == "3":
                try:
                    indice = int(input("Digite o número do produto a ser alterado: ")) - 1
                    novo_produto = input("Digite o novo nome do produto: ")
                    self.alterar_produto(indice, novo_produto)
                except ValueError:
                    print("Por favor, insira um número válido.")
            elif opcao == "4":
                print("Saindo do sistema de controle de estoque.")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = ControleEstoque()
    sistema.executar()