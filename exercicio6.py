import time
import random
import datetime

def voto(num):
    if num>2008:
        return False
    else:
        return True
ano = random.randint(1945, datetime.datetime.now().year)
print(f'O ano de nascimento eh {ano}!')
time.sleep(0.5)
if voto(ano):
    if ano==2007 or ano==2008:
        print(f'Seu voto eh opcional, pois tem {datetime.datetime.now().year-ano} anos')
        time.sleep(0.5)
    else:
        print(f'Voce esta apto a votar, pois tem {datetime.datetime.now().year-ano} anos.')
else:
    time.sleep(0.5)
    print(f'Voce nao esta apto a votar, pois tem {datetime.datetime.now().year-ano} anos.')