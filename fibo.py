# números en serie de fibonacci

def fib(n):    # Escribir la serie de fibonacci de n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # retornar la serie de fibonacci hasta n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
