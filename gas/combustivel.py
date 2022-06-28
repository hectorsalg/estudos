A = 3.45
G = 4.53

vendaA = float(input('Informe o número de litros de Álcool vendido: '))
vendaG = float(input('Informe o número de litros de Gasolina vendido: '))

if vendaA <= 20:
    descontoA = A * 3/100
    contaA = vendaA * A - descontoA
    print(f'Valor a ser pago são de R$ {contaA:.2f}')
else:
    descontoA = A * 5/100
    contaA = vendaA * A - descontoA
    print(f'Valor a ser pago são de R$ {contaA:.2f}')

if vendaG <= 20:
    descontoG = G * 4/100
    contaG = vendaG * G - descontoG
    print(f'Valor a ser pago são de R$ {contaG:.2f}')
else:
    descontoG = 3.45 * 6/100
    contaG = vendaG * G - descontoG
    print(f'Valor a ser pago são de R$ {contaG:.2f}')
