def count_ones(n):
    if not(isinstance(n, int)):
        raise TypeError

    if not(n >= 0):
        raise ValueError


    count_one = 0
    while n != 0:
        if n % 2 == 1:
            count_one += 1

        n = n // 2

    return count_one






