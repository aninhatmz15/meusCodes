# exercicio antecessor e sucessor
n = int(input('Digite um numero: '))
a = n - 1 #antecessor
s = n + 1 #sucessor
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n,a,s))
# obs: posso tirar as variaveis a e n e colocar .format(n, (n-1), (n+1)))