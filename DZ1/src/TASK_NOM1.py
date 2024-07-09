def sum_Even(lst: list) -> float:

    if not(isinstance(lst, list)):
        raise TypeError


    if len(lst) > 10 ** 5:
        raise ValueError

    for i in lst:
        if (i > 2 * 10 ** 4) or (i < -2 * 10 ** 4):
            raise ValueError

    S = 0

    for i in lst:
        if i % 2 == 0:
            S += i

    if S >= 0:
        return S

    return 1




print(sum_Even([1, 2, 3]))
