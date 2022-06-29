limite = int(input('Informe o limite do Fibonacci: '))
fib1 = 0
fib2 = 1
aux = 1
i = 0

while i < limite:
    print(aux, end = " ")
    aux = fib1 + fib2
    fib1 = fib2
    fib2 = aux
    i += 1