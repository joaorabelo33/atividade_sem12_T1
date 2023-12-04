
#Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
#preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e
#calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o
#carro à vista.

def calcula_juros_sobre_capital(capital, juros_do_capital, valor_do_bem, juros_do_bem):
    quantidade_mes = 0
    while(valor_do_bem > capital):
        capital += capital * juros_do_capital/100
        valor_do_bem += valor_do_bem * juros_do_bem/100
        quantidade_mes += 1
    return quantidade_mes    
    

def main():
    valor_do_bem = input().strip()
    valor_do_bem = int(valor_do_bem)
    juros_bem = 0.4
    capital = 10000
    juros_capital = 0.7
    
    resultado = calcula_juros_sobre_capital(capital, juros_capital, valor_do_bem, juros_bem)

    print(resultado)

if __name__ == '__main__':
    main()