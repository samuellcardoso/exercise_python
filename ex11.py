import random

# Adivinha numero
def adivinha_numero():
    numero_sorteado = random.randint(1, 10)
    chances = 3
    
    while chances > 0:
        try:
            palpite = int(input('Qual o seu palpite?\n'))

            if palpite == numero_sorteado:
                print(f'Acertou! O numero sorteado era {numero_sorteado}')
                break
            elif palpite > numero_sorteado:
                print(f'Dica: {palpite} e Maior')
                chances -= 1
                print(f'Chances: {chances}')
            elif palpite < numero_sorteado:
                print(f'Dica: {palpite} e Menor')
                chances -= 1
                print(f'Chances: {chances}')
        except ValueError:
            print('Erro... Informe apenas numeros')
adivinha_numero()

# -------------------------------------------------------------

# Quiz aleatorio
def quiz():
    quiz_data = {
        'Qual e a capital da Franca?' : 'Paris', 
        'Qual planeta e conhecido como "Planeta Vermelho"?' : 'Marte', 
        'Quem escreveu Dom Quixote?' : 'Miguel de Cervantes', 
        'Qual e o maior oceano do mundo?' : 'Oceano Pacifico', 
        'Em que ano o Brasil foi descoberto pelos portugueses?' : '1500'
    }
    perguntas = list(quiz_data.keys())

    while True:
        pergunta = random.choice(perguntas)
        resposta_correta = quiz_data[pergunta]

        print(f'Pergunta: {pergunta}')
        resposta_usuario = input('Resposta: ').strip()

        if resposta_usuario.lower() == resposta_correta.lower():
            print('Voce acertou.')
        else:
            print(f'Voce errou. A resposta correta e: {resposta_correta}')
            
        jogar_novamente = input('Jogar novamente? [s/n]: ').lower()
        if jogar_novamente != 's':
            break
quiz()
