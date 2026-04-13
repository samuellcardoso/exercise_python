import hashlib

# # Gerar o hash de uma string

def gera_hash():
    text = input('Digite um texto:\n')
    md = hashlib.md5()
    md.update(text.encode())
    print(md.hexdigest())
gera_hash()

# # ---------------------------------------------------------------

# # Comparar senhas usando sha-256

def compara_senha():
    senha = input('Informe a senha:\n')
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()

    entrada = input('Informe sua senha:\n')
    hash_entrada = hashlib.sha256(entrada.encode()).hexdigest()

    if hash_entrada == hash_senha:
        print('Senha correta!')
    else:
        print('Senha incorreta!')
compara_senha()

# # ---------------------------------------------------------------

# # Usando diferentes algoritmos de hash

def algoritmos_hash():
    text = input('Informe o texto:\n')
    algoritmos = ['md5', 'sha1', 'sha224', 'sha256', 'sha512']

    for alg in algoritmos:
        h = hashlib.new(alg)
        h.update(text.encode())
        print(f'{alg.upper()}: {h.hexdigest()}')
algoritmos_hash()

# ---------------------------------------------------------------

# Sistema simples de autenticação com hash

def autenticacao():
    usuarios = {}
    
    usuario = input('Usuario:\n')
    senha = input('Senha:\n')
    
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios[usuario] = hash_senha

    if usuario in usuarios and usuarios[usuario] == hash_senha:
        print('Login bem-sucedido!')
autenticacao()