import re

def verifica_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("Senha deve ter pelo menos 8 caracteres")

    if not re.search(r'[a-z]', senha):
        erros.append("Senha deve ter pelo menos 1 letra minúscula")

    if not re.search(r'[A-Z]', senha):
        erros.append("Senha deve ter pelo menos 1 letra maiúscula")

    if not re.search(r'[0-9]', senha):
        erros.append("Senha deve ter pelo menos 1 número")

    if not re.search(r'[^a-zA-Z0-9]', senha):
        erros.append("Senha deve ter pelo menos 1 caractere especial")
        
    if erros:
        print("Problemas encontrados:")
        for erro in erros:
            print("-", erro)
        return False
    else:
        print("Senha Forte!")
        return True

senha = input("Digite sua senha:\n")
verifica_senha(senha)
