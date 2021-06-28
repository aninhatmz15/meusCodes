'''O mesmo professor do desafio anterior quer sortear a ordem
 de apresentacao de trabalhos de aunos. Faça um programa que 
 leia o nome dos quatro alunos e mostre a ordem sorteada'''
import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Primeiro nome: '))
n3 = str(input('Primeiro nome: '))
n4 = str(input('Primeiro nome: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('='*12,'SORTEIO DA TURMA','='*12)
print('A ordem de apresentação será')
print(lista)
#SHUFFLE = EMBARALHAR
'''#######SEGUNDA SOLUCAO #########
from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Primeiro nome: '))
n3 = str(input('Primeiro nome: '))
n4 = str(input('Primeiro nome: '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)'''