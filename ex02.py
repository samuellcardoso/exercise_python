def substitui_caracter(name):
    first_caract = name[0]
    new_name = first_caract + name[1:].replace(first_caract, '$')
    print(new_name)

# -----------------------------------------------

def gera_string(name):
    name_split = name.split(' ')
    first_word = name_split[0][:2]
    first_word_rest = name_split[0][2:]
    second_word = name_split[1][:2]
    second_word_rest = name_split[1][2:]

    new_first = second_word + first_word_rest
    new_second = first_word + second_word_rest

    print(new_first, new_second)


name = input('Informe a palavra:\n')

# Escolha qual rodar
# substitui_caracter(name)
gera_string(name)