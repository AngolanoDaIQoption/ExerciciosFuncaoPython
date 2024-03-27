import time

def valores(* num):
    print(f'Analisando os valores passados...')
    time.sleep(0.3)
    print(f'{num} foram os valores passados, e foram {len(num)} valores passados!')
    time.sleep(0.5)
    print(f'O maior valor informado foi {max(num)}')

valores(4,5,6,7,10,23,2,24,56)
valores(10,20,21,32,320,4231,124124)