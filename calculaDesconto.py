'''Faça um algoritmo que leia o preço de
um produto e mostre seu novo preço, com 5% de desconto
R$10,00 = 100% e x = 100%
faz a regra de 3 e multiplica 10 por 5 e 100 por x
 o 100 que está multiplicando de um lado passa pro outro dividindo
 entao, o x seria 10x5/100'''
preco = float(input('Qual é o preço do produto? R$ '))
novoPreco = preco - (preco * 5 / 100)  
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preco, novoPreco))
