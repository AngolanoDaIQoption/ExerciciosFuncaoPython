total = dict()

def notas(* num, sit=False):
    """
    --> funcao para analisar notas e situacoes de varios alunos.
    :param num: uma ou mais notas de alunos
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma
    """
    total['Total']= len(num)
    total['Maior']= max(num)
    total['Menor']= min(num)
    media = sum(num)/len(num)
    total['Media']= round(media,2)
    print(total)
    if sit==True:
        if 7>media>5:
            print('A situacao esta aceitavel!')
        if media>7:
            print('A situacao esta boa!')
        if media<5:
            print('A situacao esta horrivel. Estudem mais!')

notas(7.0, 6.4, 6, 8, 9, sit=True)
help(notas)