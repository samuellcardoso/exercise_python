numeros = [3, 8, 5, 12, 7]
def analisar_lista():
    sum_pares = sum(n for n in numeros if n % 2 == 0)
    sum_impares = sum(n for n in numeros if n % 2 == 1)
    maior = max(numeros)
    print(f'Soma dos pares: {sum_pares}')
    print(f'Soma dos impares: {sum_impares}')
    print(f'Maior numero: {maior}')


# -------------------------------------------------------

import winsound
import time
def lanca_foguete():
    for c in range(10, -1, -1):
        time.sleep(1)
        print(c)
        if c == 0:
            print('Lancamento de foguete')
            winsound.Beep(1000, 1000)

# -------------------------------------------------------

def tabuada():
    num = int(input('Informe o numero para tabuada:\n'))
    print(f'Tabuada do {num}')
    for n in range(1, 11):
        print(f'{num} x {n} = {num * n}')


# Escolha qual rodar
# analisar_lista()
lanca_foguete()
# tabuada()