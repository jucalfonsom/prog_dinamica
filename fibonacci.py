def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo (n - 2)


if __name__ == "__main__":
    n = int(input('Escribe un número para calcular el fibonacci: '))
    resultado = fibonacci_recursivo(n)

    print(f'El resultado es: {resultado}')