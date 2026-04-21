def antecessor_sucesspor():
    num = int(input('Informe o numero:\n'))
    print(f'Antecessor: {num - 1} | Numero: {num} | Sucessor: {num + 1}')

# -----------------------------------------------------------

def calcular_media():
    notas = []
    while len(notas) < 4:
        nota = float(input('Informe a nota:\n'))
        notas.append(nota)
        
    media = sum(notas) / len(notas)
    print(f'Media: {media}')

# Escolha qual rodar
calcular_media()
# antecessor_sucesspor()