# Faça um programa que tenha uma Função chamada contador(), que receba tres parâmetros:
# inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar très contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) Da 10 até 0, de 2 em 2
# c) Uma contagem personalizada.
import time
def contador(i, f, p):
    """
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: de quanto em quanto vai ser pulado
    :return: retorna
    """
    print('-'*30)
    print('Contagem de 1 ate 10 de 1 em 1: ')
    for c in range(1,11):
        print(c, end=' ')
        time.sleep(0.3)
        print(' ')
    print('-' * 30)
    print('Contagem de 10 ate 0 de 2 em 2: ')

    cont = 10
    for c in range(1,7):
        print(cont)
        time.sleep(0.3)
        cont-=2
    print('-' * 30)
    print('Agora eh a sua vez de personalizar a contagem!')
    a = int(input('Inicio: '))
    b = int(input('Fim: '))
    c = int(input('Passo: '))
    print(f'Contagem de {a} ate {b} de {c} em {c}')
    print('-' * 30)
    contrario = a
    if a <= b:
        for v in range(a, b+1, c):
            print(v, end=' ')
            time.sleep(0.3)
    else:
        for v in range(a, b-1, -c):
            print(contrario, end=' ')
            time.sleep(0.3)
            contrario -= c
contador(0,0,0)