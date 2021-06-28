'''Mostre se um triangulo será:
EQUILATERO: todos os lados iguais
ISÓSCELES: dois lados iguais
ESCALENO: todos os lados diferentes'''
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')

''' nesse exercicio foi utilizado
if dentro de if, == sem and, pois 
o python permite e uma obs:
end='' que significa que nao tem enter 
no fim da linha pra o proximo print'''
