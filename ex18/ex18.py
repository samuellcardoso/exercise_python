import csv
import os

caminho_arquivo = 'ex18/alunos.csv'

def ler_arquivo():
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                nome = linha['Nome']
                idade = linha['Idade']
                nota = linha['Nota']

                print(f'Aluno: {nome} | Idade: {idade} | Nota: {nota}')
    except FileNotFoundError:
        print(f'Erro... O arquivo {caminho_arquivo} nao foi encontrado')

# ---------------------------------------------------------------

def escrever_dados():
    if not os.path.exists('ex18'):
        os.makedirs('ex18')

    name_arquivo = input('Nome do arquivo:\n')
    caminho = f'ex18/{name_arquivo}'
    
    if not os.path.exists(caminho):
        with open(caminho, 'w', newline='') as arquivo:
            write = csv.writer(arquivo, lineterminator='\n')
            write.writerow(['Nome', 'Preco', 'Quantidade'])
            print(f'Arquivo {name_arquivo} criado com sucesso.')
    else:
        print('Arquivo ja existe. Adicionando novos itens...')
    
    while True:
        print('--- Cadastro de Produtos ---')
        name = input('Produto (ou digite "sair" para encerrar):\n')
        
        if name.lower() == 'sair':
            break
        
        try:
            price = float(input('Preco:\n'))
            quantidade = int(input('Quantidade:\n'))
        except ValueError:
            print('Erro... Somente numeros.')
            continue
        
        with open(caminho, 'a', newline='') as items:
            write = csv.writer(items, lineterminator='\n')
            write.writerow([name, price, quantidade])
            print('Dados gravados com sucesso.')
            
        continuar = input('Cadastrar outro produto? (s/n):').lower()
        if continuar == 'n':
            break
        
    print(f'Verifique o arquivo em: {caminho}')
    
# ---------------------------------------------------------------

def calcular_estatisticas():
    caminho = 'ex18/vendas.csv'
    total = 0

    with open(caminho, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            quantidade = int(row['quantidade'])
            valor_unitario = float(row['valor_unitario'])
            total_item = quantidade * valor_unitario
            
            print(f'Produto: {row["produto"]} - Total: {total_item:.2f}')
            
            total += total_item
        print(f'Valor total de todas as vendas: {total:.2f}')

# ---------------------------------------------------------------

# Escolha qual rodar

# ler_arquivo()
# escrever_dados()
calcular_estatisticas()