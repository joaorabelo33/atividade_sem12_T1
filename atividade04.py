#O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um
#programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8
#dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989
#e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).

def calcula_numero_da_sorte(data):
    numero_da_sorte = 0
    
    while(data):
        numero_da_sorte += data % 10
        data = data // 10

    return numero_da_sorte


def main():
    data_de_nascimento = input()
    data_de_nascimento = int(data_de_nascimento)

    resultado = calcula_numero_da_sorte(data_de_nascimento)
    
    print(resultado)

if __name__ == '__main__':
    main()