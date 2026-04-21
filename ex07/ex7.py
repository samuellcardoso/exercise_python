from strings import inverte_string, string_indice_par, string_indice_impar

def menu():
    frase = input('Informe a frase:\n')

    opcoes = [
        'Inverter string',
        'Letras com indice par',
        'Letras com indice impar',
        'Sair'
    ]
    
    while True:
        print('-'*30)
        for i, opcao in enumerate(opcoes, start=1):
            print(f'{i}-{opcao}')
        print('-'*30)
            
        try:
            choice = int(input('Escolha uma das opcoes:\n'))

            if choice == 1:
                print(inverte_string(frase))
            elif choice == 2:
                print(string_indice_par(frase))
            elif choice == 3:
                print(string_indice_impar(frase))
            elif choice == 4:
                print('Saindo...')
                break
            else:
                print('Erro... Opcao invalida.')
        except ValueError:
            print('Erro... Digite o indice valido.')
menu()