peso = float(input('Informe a quantidade de Quilos: '))

print('')

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

print(f'A quantidade de quilos entregue por João foi de {peso:.2f}')
print('')
if peso > 50:
    print(f'O excesso da quantidade de quilos foi de {excesso:.2f}')
    print('')
    print(f'A multa que João pagará é de R$ {multa:.2f}')
    print('')
else:
    print('Não há multa!')
