# Desenvolva um programa que fale se o número é par ou impar

numero = int(input('Digite um número: '))

#Verificar se o número é par ou impar
if numero % 2 == 0:
    print(f'{numero} é um número par.')
else:
    print(f'{numero} é um número impar.')