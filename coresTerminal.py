'''ANSI
\033[0:33:44m
     estilo(negrito,
      italico ou 0 q é nenhum)
      em seguida o codigo de texto
      e o codigo de fundo 
todas as cores começam com \033
style: 0 none, 1 bold, 4 underline, 7 negative 
text: 30,31,32,33,34,35,36,37
(white,red,green,yelow,blue,purple,light blue,grey)
backgroung: 40,41,42,43,44,45,46,47
(white,red,green,yelow,blue,purple,light blue,grey)
\033[1;30;41m
\033[4;33;44m
\033[1;35;43m
\033[30;42m
\033[m
\033[7;30m '''

print('\033[0;30;45m*\33[m' * 15)
print('\033[1;30;43mPROGRAMA DA ANA\33[m')
print('\033[0;30;45m*\33[m' * 15)

nome = 'Ana'
cores = {'limpa':'\033[m', 
'azul':'\033[34m', 
'amarelo':'\033[33m',
 'pretoebranco':'\033[7;30m'}
print('Olá! muito prazer em conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

'''a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))'''

'''outra forma de fazer simplificado:
nome = 'Ana''
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[m', nome, '\033[m')) '''

'''se eu utilizar um 7 no lugar do formato de letras ele inverte as cores do texto e do fundo'''

