from viagem import Viagem

trip_1 = Viagem('Brasil') 
trip_2 = Viagem('Franca') 
trip_3 = Viagem('Londres') 
trip_4 = Viagem('Alemanha') 
trip_5 = Viagem('Italia') 

list_trip = [trip_1, trip_2, trip_3, trip_4, trip_5]

print('Ola viajante, temos algumas ofertas para voce.')
turista = input('Informe seu nome:\n')

print(f'{turista} temos 5 destinos que combinam com voce:')
for i, opcao in enumerate(list_trip, start=1):
    print(f'[{i}]-{opcao.destino}')

print('Escolha um dos destinos para viajar.')

while True:
    try:
        choice = int(input('> '))
        if 1 <= choice <= len(list_trip):
            print(f'{turista}, sua viagem para {list_trip[choice - 1].destino} esta marcada.')
            print('Boa viagem!')
            break
        else:
            print('Opcao invalida. Tente novamente.')
    except ValueError:
        print('Erro...Apenas numeros.')