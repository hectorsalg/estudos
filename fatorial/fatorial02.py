num = 0
numaux = 1

while numaux >= 0 and numaux < 16:
    num = int(input('Digite um número: '))
    if num < 0 or num > 15:
        print('Programa encerrado!')
        break

    if num == 0:
        print('0! = 0')
        continue

    aux = 1
    numaux = num
    while numaux > 0:
        aux *= numaux
        numaux -= 1
    print(f'{num}! = {aux}.')
