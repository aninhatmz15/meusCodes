'''Crie um programa que leia um número Real qualquer
  pelo teclado e mostre na tela a sua porção Inteira'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

'''segunda solucao:::::::
num= float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porcao inteira é {}'.format(num, int(num)))'''


