import secrets
import string
import random

def gerador_senha():
    senha_chars = []
    tamanho_senha = int(input('Qual o tamanho da senha:\n'))
    
    letra_minuscula = string.ascii_lowercase
    letra_maiuscula = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    
    senha_chars.append(secrets.choice(letra_minuscula))
    senha_chars.append(secrets.choice(letra_maiuscula))
    senha_chars.append(secrets.choice(numeros))
    senha_chars.append(secrets.choice(simbolos))

    while len(senha_chars) < tamanho_senha:
        c = secrets.choice(letra_minuscula + letra_maiuscula + numeros + simbolos)
        senha_chars.append(c)

    random.shuffle(senha_chars)
    senha = ''.join(senha_chars)

    print(senha)
gerador_senha()