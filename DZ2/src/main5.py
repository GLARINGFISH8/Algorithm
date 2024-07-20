mas = []


file = open("data")

for i in file:
    i = i.replace("2023", "").replace("-", " ").replace(",", " ").replace("\n", "")
    i = i.split(" ")
    del i[0]
    mas.append(i)



# magnitude = input("Введите Д, если хотите узнать статустику в днях. Введите Н, если хотите узнать статистику в неделях."
#                   "Введите М, елси хотите узнать статистику в месяцах")




def search_day(lst: list) -> tuple:
    worse = int(lst[0][2])
    best = int(lst[0][2])
    worse_day = lst[0]
    best_day = lst[0]

    for i in range(0, len(lst), 1):
        if int(lst[i][2]) > best:
            best = int(lst[i][2])
            best_day = lst[i]

        if int(lst[i][2]) < worse:
            worse = int(lst[i][2])
            worse_day = lst[i]

    return (best_day,  worse_day)




def create_monthMassiv(lst: list, month: str):
    month_massiv = []

    for i in range(0, len(lst), 1):
        if month == lst[i][0]:
            month_massiv.append(lst[i])

    return month_massiv





def search_week(lst: list):
    static_week = {}
    summ = 0
    lever = 0
    item = 0

    for i in range(0, len(lst), 1):

        summ += int(lst[i][2])
        lever += 1

        if lever == 7:
            item += 1
            static_week[item] = summ
            summ = 0
            lever = 0

    best = static_week[1]
    worse = static_week[1]
    best_day = 1
    worse_day = 1

    for (key, value) in static_week.items():
        if value > best:
            best = value
            best_day = key

        if value < worse:
            worse = value
            worse_day = key

    return (best_day, best, worse_day, worse)





def search_month_sum(lst: list):
    static_month = []
    lever = '01'
    summ = 0

    for i in range(0, len(lst), 1):

        if  lever == lst[i][0]:
            summ += int(lst[i][2])

            if len(lst) - 1 == lst.index(lever):
                static_month.append((lever, summ))
                return static_month

        else:
            static_month.append((lever, summ))
            summ = 0
            lever = lst[i][0]






print(search_month_sum(mas))








