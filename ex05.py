def conta_letras():
    frase = input('Informe a frase:\n')

    sum_maiuscula = sum(1 for s in frase if s.isupper())
    sum_minuscula = sum(1 for s in frase if s.islower())

    print(f'Letras Maiusculas: {sum_maiuscula}')
    print(f'Letras Minusculas: {sum_minuscula}')


# ------------------------------------------------------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def par_impar():
    par = [n for n in lista if n % 2 == 0]
    impar = [n for n in lista if n % 2 == 1]

    print(f'Numeros pares: {par} (total: {len(par)})')
    print(f'Numeros impares: {impar} (total: {len(impar)})')


# Escolha qual rodar
# conta_letras()
par_impar()