def leiaint():
    while True:
        try:
            num = int(input('Digite um valor inteiro: '))
            return num
        except ValueError:
            print('Digite um valor inteiro válido!')

n = leiaint()
print(f'Você digitou o valor inteiro {n}')