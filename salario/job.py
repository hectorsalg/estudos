ganho = float(input('Informe a quantidade de ganho p/ hora: R$ '))
horasmes = int(input('Informe a quantidade de horas trabalhadas no mês: '))

salarioBruto = ganho * horasmes
print(f'O valor do salário bruto é de R$ {salarioBruto}.')
print('')

ir = salarioBruto * 11/100
print(f'Pagou de imposto de renda o valor de R$ {ir}.')
print('')

inss = salarioBruto * 8/100
print(f'Pagou para o INSS o valor de R$ {inss}.')
print('')

sindicato = salarioBruto * 5/100
print(f'Pagou para o Sindicato o valor de R$ {sindicato}.')
print('')

salarioLiq = salarioBruto - ir - inss - sindicato

print(f'O salário líquido ficou de R$ {salarioLiq}.')