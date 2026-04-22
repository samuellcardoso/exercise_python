import os

def criar_arquivo(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as a:
            print('Arquivo criado com sucesso.')
    else:
        print('Arquivo ja existe.')
    
def add_conteudo(arquivo, name):
    if not name.strip():
        print('Erro... Informe o conteudo.')
    else:
        with open(arquivo, 'a') as f:
            f.write(f'{name}\n')
            print('Conteudo adicionado com sucesso.')

def read_line(arquivo, qtd_line):
    if qtd_line <= 0:
        print('Erro... Nenhuma linha selecionada.')
        return

    with open(arquivo, 'r', encoding='utf-8') as f:
        for i, linha in enumerate(f, start=1):
            if i > qtd_line:
                break
            print(linha.strip())
            
def remove_arquivo(arquivo):
    try:
        os.remove(arquivo)
        print('Arquivo removido com sucesso.')
    except FileNotFoundError:
        print('Arquivo nao encontrado.')
        
        
def menu():
    arquivo = None

    while True:
        opcoes = [
            'Criar Arquivo',
            'Adicionar Conteudo',
            'Ler Linhas',
            'Excluir Arquivo',
            'Sair'
        ]
        
        for i, opcao in enumerate(opcoes, start=1):
            print(f'{i}-{opcao}')

        try:
            choice = int(input('Informe a opcao:\n'))
        except ValueError:
            print('Erro... Somente numeros.')
            continue

        if choice == 1:
            arquivo = input('Nome do arquivo:\n')
            criar_arquivo(arquivo)
        elif choice == 2:
            if not arquivo:
                print('Crie ou selecione um arquivo primeiro.')
                continue
            
            name = input('Informe o conteudo:\n')
            add_conteudo(arquivo, name)
        elif choice == 3:
            if not arquivo:
                print('Crie ou selecione um arquivo primeiro.')
                continue
            
            try:
                qtd_line = int(input('Ler quantas linhas?\n'))
                read_line(arquivo, qtd_line)
            except ValueError:
                print('Erro... Somente numeros.')
        elif choice == 4:
            arquivo_remove = input('Informe o arquivo para remover:\n')

            if not os.path.exists(arquivo_remove):
                print('Arquivo nao existe.')
                continue
                
            remove_arquivo(arquivo_remove)
            arquivo = None
        elif choice == 5:
            print('Saindo...')
            break
        else:
            print('Opcao invalida... Tente novamente.')
menu()