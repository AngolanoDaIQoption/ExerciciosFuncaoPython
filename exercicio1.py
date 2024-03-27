# Faça um programa que tenha uma Função chamada áreal(), que receba as dimensões de um
# terreno retangular (largura & comprimento) mostre a área do terreno.

def area(a, b):
    re = a*b
    print(f'A area do terreno eh de {re}M quadrados!')

lar = int(input('Insira a largura do terreno: '))
com = int(input('Insira o comprimento do terreno: '))

area(lar, com)