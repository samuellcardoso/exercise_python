# def calcula_distancia():
#     distancia_km = float(input('Informe a distancia em Km:\n'))
#     if  distancia_km <= 200:
#         print(distancia_km * 0.50)
#     else:
#         print(distancia_km * 0.35)
# calcula_distancia()

def aumento_salario():
    salario = float(input('Informe seu salario:\n'))
    if salario >= 1250:
        novo = salario * 1.10
        print(f'Salario reajustado com 10%: R${novo:.2f}')
    else:
        novo = salario * 1.15
        print(f'Salario reajustado com 15%: R${novo:.2f}')
aumento_salario()