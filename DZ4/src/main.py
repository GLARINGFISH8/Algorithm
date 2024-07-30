#№1
def  bubble_sorted(array: list, comparison = lambda one_el, two_el: one_el > two_el):

    for i in range(0, len(array), 1):
        for j in range(0, len(array) - i - 1, 1):

            if comparison(array[j], array[j + 1]):
                array[j], array[j + 1]  = array[j + 1], array[j]



    return array

#№2
def permutation_sort(array: list,  key="val", comparison = lambda one_el, two_el: one_el > two_el):

    lenght = len(array)
    compare = 0
    exchange = 0

    if lenght == 0:
        if key == "val": return array
        if key == "comp": return compare
        if key == "exc": return exchange


    if lenght == 1:
        if key == "val": return array
        if key == "comp": return 1
        if key == "exc": return 1


    if not(isinstance(array, list)):
        raise TypeError

    for i in range(0, len(array) - 1, 1):
        minn = i

        for j in range(i + 1, len(array), 1):

            compare += 1
            if comparison(array[minn], array[j]):
                minn = j

        exchange += 1
        array[i], array[minn] = array[minn], array[i]


    if key == "val": return array
    if key == "comp": return compare
    if key == "exc": return exchange

    return ValueError




# №3
def summ(array: list) -> int and float:

    if len(array) == 0:
        return 0


    S = array[0]
    array = array[1: ]
    T = summ(array) + S

    return T




# №4
def maxx(array: list) -> int and float:
    pass







# №5
def summ_chet(array: list) -> int and float:

    if len(array) == 0:
        return 0

    S = 0
    if array[0] % 2 == 0:
        S = array[0]

    array = array[1: ]
    T = summ(array) + S

    return T



