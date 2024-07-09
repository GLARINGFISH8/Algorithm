def len_Often(lst: list) -> float:

    if not(isinstance(lst, list)):
        raise TypeError

    if not lst:
        raise ValueError

    if len(lst) > 10 ** 5:
        raise ValueError

    for i in lst:
        if i > 2 * 10 ** 4 or i < 1:
            raise ValueError

    tranzit = 0
    max_len = 0
    min_num = lst[0]

    for i in range(0, len(lst), 1):
        for j in range(0, len(lst), 1):
            if lst[i] == lst[j]:
                tranzit += 1

        if max_len < tranzit:
            max_len = tranzit
            min_num = lst[i]

        if max_len == tranzit:
            if min_num > lst[i]:
                min_num = lst[i]

        tranzit = 0
    return min_num


