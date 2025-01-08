def calculadora (num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao ==2:
        return num1 - num2
    elif operacao ==3:
        return num1*num2
    elif operacao ==4:
        if num2!=0:
            return num1/num2
    else:
        return "ERRO: Divisão por zero!"

# Exemplo de uso
resultado = calculadora(10, 5, 1)  # Soma
print("Resultado:", resultado)

resultado = calculadora(10, 5, 4)  # Divisão
print("Resultado:", resultado)

resultado = calculadora(10, 5, 5)  # Operação inexistente
print("Resultado:", resultado)