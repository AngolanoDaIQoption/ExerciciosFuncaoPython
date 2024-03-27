import time
import random

numeros = list()
numerospares= list()

def sorteio():
    print('Sorteando 5 numeros: ', end='')
    for c in range(1,6):
        num = random.randint(1,21)
        time.sleep(0.3)
        print(f'{num}', end=' ')
        numeros.append(num)
        if num%2==0:
            numerospares.append(num)
    print(f'Somando os numeros pares da lista {numeros}, temos {sum(numerospares)}')

sorteio()

