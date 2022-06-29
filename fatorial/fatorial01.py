from re import I


num = int(input('Digite um número: '))
numaux = num
aux = 1

while numaux > 0:
    aux *= numaux
    numaux -= 1


print(f'{num}! = {aux}.')