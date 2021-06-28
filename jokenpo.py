'''Crie um programa que faça o
computador jogar jokenpô
com você'''
from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ]PEDRA
[ 1 ]PAPEL
[ 2 ]TESOURA''')
jogador = int(input('Qual é a jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!!')
print('=-' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada inválida') 
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida') 

elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida') 



'''random:  maquina 
escolhe um valor para vc'''

