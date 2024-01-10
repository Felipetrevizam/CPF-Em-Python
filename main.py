import random


def gerar_cpf():
    # Gerar os primeiros 9 números de formar aleatória
    num = [random.randint(0, 9) for _ in range(9)]

    # Gerar primeiro digito verificador
    sum_of_products = sum((num[index] * (10 - index) for index in range(9)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    num.append(expected_digit)

    # Gerar segundo digito verificador
    sum_of_products = sum((num[index] * (11 - index) for index in range(10)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    num.append(expected_digit)

    # Formatar o número do CPF
    num = "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*num)

    return num


def validar_cpf(numero):
    # Utilizar os dois últimos dígitos para validar o CPF
    numero = [int(digit) for digit in numero if digit.isdigit()]

    # Verificar se o CPF tem 11 dígitos e se não é formado por uma sequência de dígitos iguais
    if len(cpf) != 11 or numero == numero[::-1]:
        return False

    # Cálculo do primeiro dígito verificador
    sum_of_products = sum((numero[index] * (10 - index) for index in range(9)))
    expected_digit = (sum_of_products * 10 % 11) % 10

    if numero[9] != expected_digit:
        return False

    # Cálculo do segundo dígito verificador
    sum_of_products = sum((numero[index] * (11 - index) for index in range(10)))
    expected_digit = (sum_of_products * 10 % 11) % 10

    if numero[10] != expected_digit:
        return False

    return True


while True:
    resposta = input("Você quer validar um CPF? (V)\nOu você quer gerar um CPF? (G)\nVocê quer sair do programa? (S)\n")

    if resposta == 'V' or resposta == 'v':
        cpf = input("Digite o CPF: ")
        # Verificar se o cpf tem 11 dígitos, ignorando todos o '.' e '-'
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) != 11:
            print('CPF inválido por não ter todos os dígitos')
        else:
            if validar_cpf(cpf):
                print('CPF válido\n')
            else:
                print('CPF inválido\n')

    elif resposta == 'G' or resposta == 'g':
        novo = gerar_cpf()
        print(f'CPF: {novo}\n')

    elif resposta == 'S' or resposta == 's':
        print('\n' + '\033[1m' + 'Saindo' + '\033[1m' + '\n')
        break

    else:
        print('Opção inválida')
