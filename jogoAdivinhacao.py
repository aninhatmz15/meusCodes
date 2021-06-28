'''Escreva um numero que faça o computador pensar
 em um numero inteiro entre 0 e 5 e peça 
 para o usuario tentar descobrir qual foi 
 o numero escolhido pelo computador. 
 O programa deverá escrever na tela se
  o usuário venceu ou perdeu'''
#randint vai randomizar um numero inteiro
#random vai fazer o pc escolher um numero p mim
from random import randint
from time import sleep #o sleep faz o computador esperar um pouco para dar a resposta
computador = randint(0,5) #Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei? ')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(3) #3 seriam 3 segundos pro usuário aguardar
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador,jogador))



