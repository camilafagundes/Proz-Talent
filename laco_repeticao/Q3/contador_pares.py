#Desenvolva um programa que só deve aceitar números pares. 
def aceitar_apenas_pares():
    while True:
        try:
            # Solicita um número ao usuário
            numero = input("Digite um número par: ")

            # Converte a entrada para inteiro
            numero = int(numero)

            # Verifica se o número é par
            if numero % 2 == 0:
                print(f"Você digitou o número par: {numero}")
                break
            else:
                print("Você digitou um número ímpar. Por favor, tente novamente.")
        except ValueError:
            print("Você digitou um caractere inválido. Por favor, digite apenas números pares.")

# Chama a função
aceitar_apenas_pares()