'''Crie um programa que leia duas notas
de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo
com a média atingida:
-Média abaixo de 5.0: Reprovado
-Média entre 5.0 e 6.9: Recuperação
-Média 7.0 ou superior: Aprovado'''
print('*' * 10,'\033[0;30;45mCALCULADORA DE MÉDIA \033[m', '*'* 10)
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) /2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if média >= 5 and média < 7:
    print('O aluno está em \033[0;30;43mRECUPERAÇÃO\033[m')
elif média < 5:
    print('O aluno está \033[0;30;41mREPROVADO\033[m')
elif média >= 7:
    print('O aluno está \033[0;30;42mAPROVADO\033[m')
