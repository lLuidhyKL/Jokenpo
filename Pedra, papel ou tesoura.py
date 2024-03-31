from random import randint
from time import sleep


opções = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# BASE DO JOGO

print(f'''{'JOKENPÔ':=^20}
PARA JOGAR ESCOLHA
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA
''')

jogador = int(input('Sua escolha: '))
if jogador > 2:
    while jogador > 2:
        jogador = int(input('Escolha uma opção valida: '))

# BRINCANDO COM SLEEP
            
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('=-=-=-=-Resultado-=-=-=')

# CENARIOS POSSIVEIS

if jogador == computador:
    print('EMPATE')

if computador == 0:
    if jogador == 1:
        print('PARABÉNS VOCÊ GANHOU')
    elif jogador == 2:
        print('VOCÊ PERDEU')

if computador == 1:
    if jogador == 2:
        print('PARABÉNS VOCÊ GANHOU')
    elif jogador == 0:
        print('VOCÊ PERDEU')

if computador == 2:
    if jogador == 0:
        print('PARABÉNS VOCÊ GANHOU')
    elif jogador == 1:
        print('VOCÊ PERDEU')

# RESULTADO

print(f'''
O jogador jogou {opções[jogador]}
O computador jogou {opções[computador]}''')
