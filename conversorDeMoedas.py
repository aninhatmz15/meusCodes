'''crie um programa que leia quanto dinheiro
 uma pessoa tem na carteira e mostre 
 quantos dólares ela pode comprar
considere US$1,00=R$,27'''
real = float(input('Quanto dinheiro vc tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${:.2f} vc pode comprar US${:.2f}'.format(real,dolar))
