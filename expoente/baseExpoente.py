base = int(input('Valor da base: '))
expo = int(input('Valor da expoente: '))

# contador.
i = 1

# variável para salvar resultado.
aux = base

while i < expo:
    aux = aux * base
    i += 1

print(f'A base {base} elevado pelo expoente {expo} equivale {aux}')
