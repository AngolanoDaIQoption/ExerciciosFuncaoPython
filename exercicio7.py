import math

def fatorial(num=1):
    if decisao == 's':
        for c in range(num, 0, -1):
            print(f'{c} x ', end='')
        f = 1
        for c in range(num, 0, -1):
            f*=c
        print(f'={f}')
    elif decisao == 'n':
        f = 1
        for c in range(num, 0, -1):
            f *= c
        print(f'O fatorial de {n} eh igual a {f}')
    else:
        print('Opcao invalida. Digite S ou N!')

n = int(input('Insira um numero e receba seu fatorial: '))
decisao = input('Deseja ver o calculo completo? S/N: ').lower()

fatorial(n)