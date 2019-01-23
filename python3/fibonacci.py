

def fibonacci_naive(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n):
    fib_minus_1 = 1
    fib_minus_2 = 0

    for i in range(2, n + 1):
        fib = fib_minus_1 + fib_minus_2
        fib_minus_1, fib_minus_2 = fib, fib_minus_1

    return fib
