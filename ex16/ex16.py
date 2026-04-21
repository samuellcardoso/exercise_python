from contact_book import ContactBook
from contact import Contact
import re

contact_book = ContactBook()

print('--- Agenda de Contatos ---')
while True:
    opcoes = [
        'Adicionar contato',
        'Listar contatos',
        'Buscar contato',
        'Remover contato',
        'Sair'
    ]
    
    for i, opcao in enumerate(opcoes, start=1):
        print(f'{i}-{opcao}')

    print('Escolha uma das opcoes:')
    try:
        choice = int(input('> '))
    except ValueError:
        print('Erro...Somente numeros.')
        continue

    if choice == 1:
        name = input('Nome:\n')
        email = input('Email:\n')
        phone = input('Phone:\n')

        phone_re = re.fullmatch(r'\d{4,5}-\d{4}', phone)
        email_re = re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

        if phone_re and email_re:
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
            print('Contato adicionado com sucesso.')
        else:
            print('Telefone ou email invalido.')
    elif choice == 2:
        contact_book.display_contacts()
    elif choice == 3:
        name = input('Procure por um nome:\n')
        contact = contact_book.search_contact(name)
    elif choice == 4:
        name = input('Informe o nome para remover:\n')
        contact = contact_book.search_contact(name)
        if contact:
            contact_book.remove_contact(contact)
            print('Contato removido com sucesso.')
    elif choice == 5:
        print('Saindo...')
        break
    else:
        print('Opcao invalida...Tente novamente.')