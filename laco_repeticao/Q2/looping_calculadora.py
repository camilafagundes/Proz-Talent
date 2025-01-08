def calculadora():
    while True:
        # Exibe o menu de operações
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        # Solicita a operação do usuário
        opcao = input("Digite o número da operação desejada: ")

        if opcao == "0":
            print("Saindo... Obrigado por usar a calculadora!")
            break
        elif opcao in {"1", "2", "3", "4"}:
            try:
                # Solicita os números do usuário
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                # Realiza a operação correspondente
                if opcao == "1":
                    resultado = num1 + num2
                    print(f"Resultado da soma: {resultado}")
                elif opcao == "2":
                    resultado = num1 - num2
                    print(f"Resultado da subtração: {resultado}")
                elif opcao == "3":
                    resultado = num1 * num2
                    print(f"Resultado da multiplicação: {resultado}")
                elif opcao == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado da divisão: {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida!")
            except ValueError:
                print("Erro: Você precisa digitar números válidos!")
        else:
            print("Essa opção não existe. Tente novamente.")

# Executa a calculadora
calculadora()
