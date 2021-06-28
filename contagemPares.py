'''Crie um programa que mostre
na tela todos os números pares
que estão no intervalo entre 1
e 50'''

''' o end=' ' permite printar
 o range 1 numero do lado do
outro'''

'''for n in range(1, 50):
    print('.', end='')
    if n % 2 == 0: 
        print(n, end=' ')''' #ou print('{} '.format(n), end=' ')

for n in range(2, 51, 2): #esse ultimo numero 2 significa que a iteração é pulando de 2 em 2
    print(n, end=' ')
print('Acabou')