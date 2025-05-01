def dados_usuario():
    ano_atual=2022
    nome=input("Digite seu nome completo:").strip()

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                idade = ano_atual - ano_nascimento
                print(f"\n{nome}, você completou ou completará {idade} anos em {ano_atual}.")
                break
            else:
                print("Ano inválido! O ano de nascimento deve estar entre 1922 e 2021.")
        except ValueError:
            print("Erro! Você deve digitar um número válido para o ano de nascimento.")

# Executa o programa
dados_usuario()
