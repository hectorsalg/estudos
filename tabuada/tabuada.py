num = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
final = int(input('Terminar por: '))

print(f'Vou montar a Tabuada de {num} começando em {inicio} e terminar em {final}:')

while inicio <= final:
    print(f'{num} x {inicio} = {num * inicio}')
    inicio += 1