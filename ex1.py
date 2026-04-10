# num = int(input('Informe o numero:\n'))
# print(f'Antecessor: {num - 1} | Numero: {num} | Sucessor: {num + 1}')

notas = []
def calcular_media():
    while len(notas) < 4:
        nota = float(input('Informe a nota:\n'))
        notas.append(nota)
        
    media = sum(notas) / len(notas)
    print(f'Media: {media}')

calcular_media()
