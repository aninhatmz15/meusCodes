'''Faça um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra "A", 
que posicao ela aparece a primeira vez, 
que posicao ela aparece a ultima vez'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase. '.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))
#rfind: procure a partir do lado direito (right find)


