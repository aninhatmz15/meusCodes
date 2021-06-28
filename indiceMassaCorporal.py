'''Desenvolva uma lógica que leia o peso
e a altura de uma pessoa, calcule o IMC 
e mostre seu status, de acordo com a tabela
abaixo:
abaixo de 18.5: abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida'''
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) ' ))
imc = peso / (altura ** 2)
print('o IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
