# Conta Bancaria
def conta_bacaria():
    class ContaBancaria:
        def __init__(self, titular, saldo = 0):
            self.titular = titular
            self.saldo = saldo

        def __str__(self):
            return f'Titular: {self.titular} | Saldo: {self.saldo:.2f}'

        @property
        def titular(self):
            return self.__titular

        @titular.setter
        def titular(self, titular):
            if not isinstance(titular, str):
                raise ValueError('O nome precisa ser uma String.')
            self.__titular = titular
            
        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, saldo):
            if not isinstance(saldo, (int, float)):
                raise ValueError('O valor tem que ser Int ou Float.')
            self.__saldo = float(saldo)
            
        def depositar(self, valor):
            if valor <= 0:
                print('Operacao Invalida. Valor insuficiente para deposito')
            else:
                self.__saldo += valor
                print(f'Deposito de {valor:.2f} realizado com sucesso.')
            
        def sacar(self, valor):
            if 0 >= valor > self.__saldo:
                print('Operacao Invalida. Valor insuficiente para saque')
            else:
                self.__saldo -= valor
                print(f'Saque de {valor:.2f} realizado com sucesso.')
            
        def mostra_valor(self):
            print(f'Saldo atual: {self.__saldo:.2f}')

    def menu():
        print('--- Conta Bancaria ---')
        print(f'Bem vindo(a), {c.titular}!')
        

        opcoes = [
            'Depositar',
            'Sacar',
            'Mostrar saldo',
            'Sair'
        ]
        print('-'*30)

        for i, opcao in enumerate(opcoes, start=1):
            print(f'{i}-{opcao}')

        print('-'*30)

        while True:
            print(f'Saldo: {c.saldo}\n')
            print('Informe a opcao')
            try:
                choice = int(input('> '))

                if choice == 1:
                        valor = float(input('Valor de deposito:\n'))
                        c.depositar(valor)
                elif choice == 2:
                        valor = float(input('Valor de saque:\n'))
                        c.sacar(valor)
                elif choice == 3:
                    c.mostra_valor()
                elif choice == 4:
                    print('Saindo da conta.')
                    break
                else:
                    print('Erro...Informe a opcao correta.')
            except ValueError:
                print('Erro...Somente numeros.')

    nome = input('Nome do titular:\n')
    saldo = float(input('Saldo da conta:\n'))
    c = ContaBancaria(nome, saldo)
    menu()

# --------------------------------------------------------------

# Cadastro de Animais
from collections import Counter
def cadastro_animais():
    class Animal():
        def __init__(self, name, category, size):
            self.name = name
            self.category = category
            self.size = size

        def __str__(self):
            return f'Animal: {self.name} | Categoria: {self.category} | Tamanho: {self.size} metros.'
        
    class Cachorro(Animal):
        def falar(self):
            return f'O cachorro {self.name} diz: Au Au Au...!!!'

    class Gato(Animal):
        def falar(self):
            return f'O gato {self.name} diz: Miiaaauuu...!!!'
        
    class Zoo:
        def __init__(self):
            self.list_animals = []

        def add_animal(self, animal):
            self.list_animals.append(animal)

    zoo = Zoo()

    while True:
        opcoes = [
            'Cachorro',
            'Gato',
            'Sair'
        ]

        for i, opcao in enumerate(opcoes, start=1):
            print(f'{i}-{opcao}')

        try:
            choice = int(input('Escolha uma das opcoes:\n'))
        except ValueError:
            print('Erro...Somente numeros!')
            continue
        
        if choice == 3:
            print('Saindo...')
            break
        
        if choice not in [1, 2]:
            print('Opcao invalida!')
            continue
        
        name = input('Nome:\n')
        category = input('Categoria:\n')
        size = input('Tamanho:\n')

        if choice == 1:
            zoo.add_animal(Cachorro(name, category, size))
        elif choice == 2:
            zoo.add_animal(Gato(name, category, size))
        else:
            print('Opcao invalida...')

    print('--- Lista de Animais Cadastrados ---')

    for animal in zoo.list_animals:
        print(f'{animal} | Som: {animal.falar()}')
        
    categorias = [animal.category for animal in zoo.list_animals] 
    contagem = Counter(categorias)
        
    print('--- Resumo por Categoria ---')
    for categoria, total in contagem.items():
        print(f'No zoo tem {total} animal(is) da categoria: {categoria}')

# --------------------------------------------------------------

# Calculo de Area
from abc import ABC, abstractmethod

import math
def calculo_area():
    class FormaGeometrica(ABC):
        @abstractmethod
        def calcular_area(self):
            pass
            
    class Quadrado(FormaGeometrica):
        def __init__(self, lado):
            self.lado = lado
        
        def calcular_area(self):
            return self.lado * self.lado
            
    class Circulo(FormaGeometrica):
        def __init__(self, raio):
            self.raio = raio

        def calcular_area(self):
            return math.pi * (self.raio ** 2)
        
    formas = [Quadrado(4), Circulo(3)]
    for forma in formas:
        print(f'Area: {forma.calcular_area():.2f}')

# Escolha qual exercicio rodar:
conta_bacaria()
# cadastro_animais()
# calculo_area()
