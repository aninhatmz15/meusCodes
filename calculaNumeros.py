'''Faça um programa que calcule soma,
produto, divisão, divisão inteira e produto'''
n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, \n o produto é {}, \n divisão é {:.3f}' .format(s,m,d))
print('Divisão inteira {} e potencia {}'.format(di, e))
'''end=' ' esse comando significa pra manter 
 na mesma linha qd for executado
 end='>>>'vai manter na mesma linha e printar essas setas antes 
 {:.3f} significa para manter apenas 3 casas depois do ponto flutuante
 {:>20} alinha a direita com espaco de 20 caracteres
 {:20} espaco de 20 caracteres a esquerda
 {:<20} alinhado a esquerda c espaco de 20
 {:ˆ20} centraliza o espaco 20 de cada lado
 se eu escrever {:=ˆ20} ele vai printar tipo ======Ana======='''
