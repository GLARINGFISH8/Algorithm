def find_Part(lst: list, target: int, lever="value") -> list:

    if not(isinstance(lst, list)):
        raise TypeError

    if not lst:
        raise ValueError

    if len(lst) >= 104 or len(lst) <= 2:
        raise ValueError

    if target >= 109 or target <= -109:
        raise ValueError

    for i in lst:
        if i >= 109 or i <= -109:
            raise ValueError



    for i in range(0, len(lst) - 1, 1):
        if lst[i] + lst[i + 1] == target:

            if lever == "value":
                return [lst[i], lst[i + 1]]

            if lever == "index":
                return [i, i + 1]



print(find_Part([2, 5, 6], 7, "index"))