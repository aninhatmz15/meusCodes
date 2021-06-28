'''hoje, vamos utilizar o módulo import, para
 importar bibliotecas para o programa
vamos supor q tenho 3 diretórios: bebidas, comida, doce
 import bebidas importa o diretorio bebidas
 from doce import pudim, importa somente 1 doce
  que vai estar no diretorio de doces
 biblioteca math: 

 ceil: faz arredondamento pra cima, 
 por exemplo uma media que deu 9,89 
 e vc quer arredondar pra 10
floor: arredonda pra baixo
trunc: éo truncate, ele trunca o numero, ou seja, 
elimina da virgula pra frente
pow: power, potencia funciona de forma
 semelhante aos 2 asteriscos
sqrt: calcula raiz quadrada
factorial: fatorial
 se eu colocar só import math ele importa todos
  esses da biblioteca math
from math import sqrt: faz somente a raiz
 quadrada pra mim da biblioteca math
from math import sqrt,ceil para importar duas
ou entao print('A raiz de {} é igual a {:.2f}'.format(num, math.floor(raiz))))
 terceira opcao:
from math import sqrt, floor
 dai coloca no print só floor(raiz) ao 
 invés de math.floor(raiz) e raiz= sqrt(num)''' 
import math 
num = int(input('Digite um número: ')) 
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz ))



