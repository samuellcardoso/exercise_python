import customtkinter as ctk

# Configuracao aparencia
ctk.set_appearance_mode('dark')

# Criando funcao de funcionalidade
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    # Verificar se o usuario e Samuel e senha 123456
    if usuario == 'samuel' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else:
        resultado_login.configure(text='Login incorreto', text_color='red')

# Criando Janela
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# Criando Campos
# Label
label_usuario = ctk.CTkLabel(app, text='Usuario')
label_usuario.pack(pady=10)
# Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuario')
campo_usuario.pack()
# Label
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)
# Entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack()
# Button
button = ctk.CTkButton(app, text='Login', command=validar_login)
button.pack(pady=10)
 
# Campo feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

# Iniciar a aplicacao
app.mainloop()