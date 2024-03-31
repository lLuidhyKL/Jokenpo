from random import randint
from time import sleep

jogar = 'S'
userScore = pcScore = empate = 0

while jogar in 'S':
    opções = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)

# VALIDANDO ESCOLHA

    print(f'''\033[31;40m{'JOKENPÔ':=^20}
PARA JOGAR ESCOLHA
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
      \033[m''')

    jogador = int(input('Sua escolha: '))
    if jogador > 2:
        while jogador > 2:
            jogador = int(input('Escolha uma opção valida: '))

# BRINCANDO COM SLEEP

    sleep(1)
    print('\033[30;40mJO\033[m')
    sleep(1)
    print('\033[30;40mKEN\033[m')
    sleep(1)
    print('\033[30;40mPÔ\033[m')
    sleep(1)
    print('\033[31;40m=-=-=-=-Resultado-=-=-=\033[m')

# CENARIOS POSSIVEIS

    if jogador == computador:
        print('\033[33mEMPATE\033[m')
        empate =+ 1

    if computador == 0:
        if jogador == 1:
            userScore += 1
            print('\033[32;40mPARABÉNS VOCÊ GANHOU\033[m')
        elif jogador == 2:
            pcScore += 1
            print('\033[36;40mVOCÊ PERDEU\033[m')

    if computador == 1:
        if jogador == 2:
            userScore += 1
            print('\033[32;40mPARABÉNS VOCÊ GANHOU\033[m')
        elif jogador == 0:
            pcScore += 1
            print('\033[36;40mVOCÊ PERDEU\033[m')

    if computador == 2:
        if jogador == 0:
            userScore += 1
            print('\033[32;40mPARABÉNS VOCÊ GANHOU\033[m')
        elif jogador == 1:
            pcScore += 1
            print('\033[36;40mVOCÊ PERDEU\033[m')

# RESULTADO

    print(f'''
O jogador jogou {opções[jogador]}
O computador jogou {opções[computador]}''')
    jogar = str(input('Quer jogar novamente? \n[S] [N] ')).upper()

# ENCERRANDO O JOGO
    
print(f'''\033[30;40m
O jogador venceu {userScore} partida(s)
O computador venceu {pcScore} partida(s)
houveram {empate} empate(s)
\033[m''')
print('Obrigrado por jogar :D')
