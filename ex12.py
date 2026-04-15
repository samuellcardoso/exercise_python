import customtkinter as ctk
import tkinter as tk

# app = tk.Tk()
# app.geometry('300x300')

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.geometry('400x400')


# ----------------------------------------------------------------------

# Caixa de selecao de cores
def select_color():
    app.title('Selecao de cores')

    red = tk.IntVar()
    blue = tk.IntVar()
    green = tk.IntVar()

    def check_color():
        for widget in app.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget('text') in ['Vermelho ativo', 'Azul ativo', 'Verde ativo']:
                widget.destroy()
        
        if red.get():
            tk.Label(app, text='Vermelho ativo', fg='red').pack()
        if blue.get():
            tk.Label(app, text='Azul ativo', fg='blue').pack()
        if green.get():
            tk.Label(app, text='Verde ativo', fg='green').pack()

    tk.Checkbutton(app, text='Vermelho', variable=red, command=check_color).pack()
    tk.Checkbutton(app, text='Azul', variable=blue, command=check_color).pack()
    tk.Checkbutton(app, text='Verde', variable=green, command=check_color).pack()

# ----------------------------------------------------------------------

# Calculadora basica
def calculadora():
    app.title('Calculadora')
    
    def calculo():
        try:
            n1 = int(entry_n1.get())
            n2 = int(entry_n2.get())
            op = entry_op.get()
            
            resultado = 0
            
            if op == '+':
                resultado = n1 + n2
            elif op == '-':
                resultado = n1 - n2
            elif op == '*':
                resultado = n1 * n2
            elif op == '/':
                if n2 != 0:
                    resultado = n1 / n2
                else:
                    resultado = 'Erro... (Div/0)'
            else:
                resultado = 'Op invalida'

            label_resultado.configure(text=f'Resultado {resultado}')
        except ValueError:
            label_resultado.configure(text='Erro: Digite numeros')

    entry_n1 = ctk.CTkEntry(app, placeholder_text='Primeiro Numero:')
    entry_n1.pack(pady=10)
    
    entry_op = ctk.CTkEntry(app, placeholder_text='Operacao (+, -, *, /):')
    entry_op.pack(pady=10)
    
    entry_n2 = ctk.CTkEntry(app, placeholder_text='Segundo Numero:')
    entry_n2.pack(pady=10)
    
    button = ctk.CTkButton(app, text='Calcular', command=calculo)
    button.pack(pady=15)
    
    label_resultado = ctk.CTkLabel(app, text='Resultado', font=('Arial', 14, 'bold'))
    label_resultado.pack(pady=10)

# ----------------------------------------------------------------------

# Escolha qual exercicio rodar:
calculadora()
# select_color()

app.mainloop()