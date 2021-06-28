'''Faça um programa que leia o nome completo de uma
  pessoa mostrando em seguida o primeiro e o ultimo
  nome separadamente'''
n = str(input('Digite seu nome completo: '))
nome = n.split()
print('#'*30)
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
print('#'*30)


