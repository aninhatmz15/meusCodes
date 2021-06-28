frase = 'Ana Caroline Tomaz'
'''print(frase[3:8]) #printa da terceira letra até a oitava
print(frase[:3]) #printa até a terceira letra
print(frase[3:]) #nao printa as 3 primeiras letras'''

print("""Lorem Ipsum is simply
dummy text of the printing
and typesetting industry. 
Lorem Ipsum has been 
the industry's standard 
dummy text ever since the 1500s
, when an unknown printer took
a galley of type and 
scrambled it to make a type 
specimen book. It has survived
not only five centuries, but also
the leap into electronic typesetting, 
remaining essentially unchanged.""")

'''print com aspas triplas escreve texto grande
sem precisar printar linha por linha
quando vc coloca . significa que aquilo é um objeto
print(frase.count('o')) vai contar quantas
vezes tem a letra 'o' minusculo na frase
print(frase.upper().count('O')) estou
pedindo pra contar a quantidade de 'o' q tem na
frase jogada pra maiuscula
print(len(frase)) conta quantos caracteres tem na frase'''
'''### frase = '  Curso em vídeo   '  
   print(len(frase.strip())) strip remove os espaços do começo
   e do fim da string ou seja, utilizando com
   o len ele vai contar os caracteres sem 
   espacos do inicio e do fim ###
#print(frase[0]) printa a primeira letra
#print(frase.replace('Caroline', 'Tomaz')) 
 o replace troca a palavra Caroline pela palavra Tomaz
#porem se eu colocar print(frase) embaixo, 
ele vai continuae printando com o Caroline 
pq nao salvou na string
#para solucionar isso tenho q declarar
  a variavel frase = frase.replace('Caroline', 'Tomaz')
#mas essa tem q declarar embaixo da 
 variavel frase já existente e depois printar print(frase)'''
'''uma string é imutável, a nao ser q eu 
utilize uma funçao de transformacao de string
 e faça uma atribuiçao
print('Curso'in frase) verifica se a palavra
 curso está dentro da frase e se estiver me retorna true
print(frase.find('Ana')) me mostra a posicao
 dessa frase na string
print(frase.lower().find('ana')) lower joga oq
 está em maiusculo para minusculo e o find procura
  a posicao da frase na string
print(frase.split()) separa as letras da frase
ou entao pode fazer dividido = frase.split() e print(dividido)
print(dividido[2][3]) vai me mostra a frase de posicao
 2 da minha frase e somente a terceira letra dela
###Fatiamento de String, Análise com len(), count(), 
find(), transformações com replace(), upper(), lower(), 
capitalize(), title(), strip(), junção com join().'''


