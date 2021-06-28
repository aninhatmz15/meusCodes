Desafio 022
' ' ' Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas
> o nome com todas as letras minúsculas
> Quantas letras ao todo (sem considerar os espaços).
> Quantas letras tem o primeiro nome. ' ' '

des = ' Desafio 022 '
print(f'{des:=^37}')

nome = str(input('\nDigite seu nome completo: ')).strip()
print(f'Tudo maiúsculo: {nome.upper()} \nTudo minúsculo: {nome.lower()}')
totall = nome.split()
print(f'Total de letras: {len("".join(totall))}')
print(f'Total de letras no primeiro nome: {len(totall[0])}')
_____________________________________________________________________________
Desafio 023
' ' ' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex.:
Digite um número: 1834

Unidade: 4  Dezena: 3
Centena: 8  Milhar: 1 ' ' '

des = ' Desafio 023 '
print(f'{des:=^37}')

num = int(input('\nDigite um número de 0 a 9999: ')).strip()
print(f'\nUnidade: {num[3]} \nDezena: {num[2]:>2} \nCentena: {num[3]} \nMilhar: {num[0]:>2}')
___________________________________________________________________________________________
Desafio 024
' ' ' Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" ' ' '

des = ' Desafio 024 '
print(f'{des:=^37}')

cidade = str(input('\nNome de alguma cidade: ')).strip().upper()
print(f'Começa com SANTO: {"SANTO" in cidade[:5]}')
________________________________________________________________________
Desafio 025
' ' ' Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. ' ' '

des = ' Desafio 025 '
print(f'{des:=^37}')

nome = str(input('\nDigite algum nome: ')).strip().upper()
print(f'Tem SILVA no nome: {"SILVA" in nome}')
________________________________________________________
Desafio 026
' ' ' Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez. ' ' '

des = ' Desafio 026 '
print(f'{des:=^37}')

frase = str(input('\nDigite alguma frase: ')).strip().upper()
print(f'Vezes que aparece a letra "A": {frase.count("A")}')
print(f'Posição que aparece a primeira vez: {frase.find("A")}')
print(f'Posição que aparece a última vez: {frase.rfind("A")}')
___________________________________________________________
Desafio 027
' ' ' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza ' ' '

des = ' Desafio 027 '
print(f'{des:=^37}')

nome = str(input('\nDigite seu nome completo: ')).strip().split()
print(f'Primeiro nome: {nome[0]} \nÚltimo nome: {nome[-1]}')
