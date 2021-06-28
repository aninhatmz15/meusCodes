#dobro, triplo e raiz quadrada
n = int(input('Digite um numero: '))
d = n * 2 #dobro
t = n * 3 #triplo
r = n ** (1/2) #raiz quadrada
'''(usa-se parentese para forçar a execucao do meio primeiro, 
 se nao ele executa a exponenciacao primeiro)'''
print('O dobro de {} vale {}'.format(n,d))
print('O triplo de {} é {}.\nA raiz quadrada de {} vale {:.2f}'.format(n,t,n,r))

'''outra possivel solucao
n = int(input('Digite um numero: '))
print('o dobro de {} vale{}'.format(n, (n*2)))
print('O triplo de {} é {}. \nA raiz quadrada de {} eh{:.2f}'.format(n, (n*3), n, (n**(1/2))))
#potencia também é representado por pow, entao posso fazer: pow(n, (1/2)'''

