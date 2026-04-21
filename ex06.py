times = []
        
def add_time():
    try:
        time = input('Informe o time que deseja adicionar:\n')
        if not time.strip():
            raise ValueError('Informe o nome do time.')

        times.append({'time': time, 'jogadores' : []})
        print(f'{time} adicionado a lista.')
    except ValueError as e:
        print(f'Erro... {e}')
        
def remove_time():
    try:
        indice_time = int(input('Informe o indice do time:\n'))
        
        if 0 <= indice_time < len(times):
            removido = times.pop(indice_time)
            print(f'Time: {removido["time"]} removido da lista.')
        else:
            print('Indice invalido, time nao encontrado.')
    except ValueError:
        print('Erro... Informe o indice correto.')
        
def display_times():
    if not times:
        print('Nenhum time cadastrado.')
    else:
        for i, t in enumerate(times):
            print(f'Indice: {i}')
            print(f'Time: {t["time"]}')
            print(f'Quantidade de Jogadores: {len(t["jogadores"])}')
        
def add_jogador():
    try:
        indice_time = int(input('Informe o indice do time:\n'))
        jogador = input('Informe o nome do jogador:\n')

        if 0 <= indice_time < len(times):
            times[indice_time]['jogadores'].append(jogador)
            print(f'{jogador} adicionado ao {times[indice_time]["time"]}')
        else:
            print('Indice invalido... Time nao encontrado.')
    except ValueError:
        print('Erro... Informe o nome do jogador.')
        
def remove_jogador():
    try:
        indice_time = int(input('Informe o indice do time:\n'))
        rm_jogador = input('Informe o nome do jogador:\n')

        if 0 <= indice_time < len(times):
            if rm_jogador in times[indice_time]['jogadores']:
                times[indice_time]['jogadores'].remove(rm_jogador)
                print(f'{rm_jogador} removido do {times[indice_time]["time"]}')
            else:
                print(f'{rm_jogador} nao encontrado no time.')
        else:
            print('Indice invalido... Time nao encontrado.')
    except ValueError: 
        print('Erro... Informe o nome do jogador.')

def display_jogador():
    try:
        indice_time = int(input('Informe o indice do time:\n'))
    
        if 0 <= indice_time < len(times):
            print(f'Jogadores do {times[indice_time]["time"]}')
            if times[indice_time]['jogadores']:
                for jogador in times[indice_time]['jogadores']:
                    print(f'- {jogador}')
            else:
                print('Nenhum jogador cadastrado.')
        else:
            print('Indice invalido... Time nao encontrado.')    
    except ValueError:
        print('Erro... Informe o indice do time.')

while True:
    opcoes = [
        'Adicionar time',
        'Remover time',
        'Listar times',
        'Adicionar Jogador em um time',
        'Remover Jogador de um time',
        'Listar Jogadores de um time',
        'Sair'
    ]
    print('-'*30)
    for i, opcao in enumerate(opcoes, start=1):
        print(f'{i}-{opcao}')
    print('-'*30)

    try:
        choice = int(input('Informe a opcao:\n'))

        if choice == 1:
            add_time()
        elif choice == 2:
            remove_time()
        elif choice == 3:
            display_times()
        elif choice == 4:
            add_jogador()
        elif choice == 5:
            remove_jogador()
        elif choice == 6:
            display_jogador()
        elif choice == 7:
            print('Saindo...')
            break
        else:
            print('Erro... Informe a opcao correta.')
    except ValueError:
        print('Erro... Digite apenas opcoes validas.')