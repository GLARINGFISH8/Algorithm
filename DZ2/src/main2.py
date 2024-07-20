def fibonacci(n: int) -> list:
    if not(isinstance(n, int)):
        raise TypeError

    if n < 0:
        raise ValueError

    numF = [0, 1]
    item = 0

    if n == 0:
        return [0]

    if n == 1:
        return numF


    for i in range(2, n + 1, 1):
        item = numF[-2] + numF[-1]
        numF.append(item)

        if item > n:
            return numF









