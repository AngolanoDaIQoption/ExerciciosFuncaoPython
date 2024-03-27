def ficha(a, b=0):
    """
    :param a: nome do jogador
    :param b: quantos gols marcou
    :return: retorna algo
    """
    if nome=='' or gols=='':
        print(f'O jogador <desconhecido> fez {b} gols no campeonato!')
    else:
        print(f'O jogador {a} marcou {b} gols no campeonato!')


nome = input('Nome do jogador: ')
gols = input('Quantos gols marcou: ')

ficha(nome, gols)


