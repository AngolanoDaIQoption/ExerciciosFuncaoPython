# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro & mostre
# uma mensagem com tamanho adaptável.

def escreva(txt):
    n = len(txt)
    print('-'*n)
    print(txt)
    print('-'*n)

escreva('Ola mundo!')
escreva('Bem vindos ao programa!')
escreva('Ja podem ir embora!')
