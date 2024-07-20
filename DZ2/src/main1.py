def factorial(n: int):
    if not(isinstance(n, int)):
        raise TypeError

    if not(0 <= n <= 20):
        raise ValueError

    if n == 0:
        return 1

    mult = 1

    for i in range(1, n + 1, 1):
        mult *= i

    return mult

print(factorial(20))

