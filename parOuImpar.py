'''Crie um programa que leia um numero inteiro
  e mostre na tela se ele é par ou ímpar
print('#'* 10,'JOGO DO PAR OU ÍMPAR', '#' * 10)'''
numero = int(input('Me diga um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))


