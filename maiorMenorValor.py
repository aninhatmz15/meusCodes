'''Faça um programa que leia
tres numeros e mostre qual é
o maior e qual é o menor'''
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando que é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#Verificando que é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor foi {}'.format(menor))
print('O maior valor foi {}'.format(maior))

