""" Four fibonacci sequence implementations, from worst to best.
"""


def fibonacci_naive(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


cache = {}

def fibonacci_cache(n):
    if n == 0 or n == 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


cache = {}

def fibonacci_iter(n):
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


def fibonacci(n):
    fib_minus_1 = 1
    fib_minus_2 = 0

    for i in range(2, n + 1):
        fib = fib_minus_1 + fib_minus_2
        fib_minus_1, fib_minus_2 = fib, fib_minus_1

    return fib
