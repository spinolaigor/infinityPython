# Solicita ao usuário o número para o qual deseja gerar a tabuada
numero = int(input('Informe o número para a tabuada (1 a 10): '))

# Verifica se o número está dentro do intervalo válido
if 1 <= numero <= 10:
    print(f'Tabuada de {numero}:')

    # Loop de 1 a 10 para gerar a tabuada
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} X {i} = {resultado}')
else:
    print('Número fora do intervalo válido (1 a 10).')
