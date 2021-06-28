'''Faça um programa que leia um angulo qualquer
 e mostre na tela o valor do seno, 
 cosseno e tangente desse angulo'''
import math 
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))
'''algoritmos programa em que o usuario digita um angulo
  e o programa lhe apresenta o seno,
cosseno e tangente desse angulo'''
''' ###### SEGUNDA SOLUCAO ########
obs: nessa segunda solucao nao precisamos referenciar o modulo math

from math import radians,sin,cos,tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo,tangente))'''
