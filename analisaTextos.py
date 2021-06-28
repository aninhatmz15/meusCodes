'''crie um programa que leia o nome 
completo de uma pessoa e mostre o 
nome com todas a letras maiusculas 
e minusculas, quantas letras ao todo 
sem contar espaços, quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome completo: ')).strip() #strip elimina os espaços antes e depois da string
print('Analisando seu nome...')
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letra'.format(len(nome) - nome.count(' '))) #esse é conta os caracteres de nome menos os espaços contados que tem
#len conta os espaços como letra colocando só ele
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
'''outra solucao #####
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))'''
