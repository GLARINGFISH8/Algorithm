
def search_day(lst: list) -> tuple:
    """находите лучший и худший день
    """
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




def create_monthMassiv(lst: list, month: str) -> list:
    """создает по указанному месяцу массив
    """
    month_massiv = []

    for i in range(0, len(lst), 1):
        if month == lst[i][0]:
            month_massiv.append(lst[i])

    return month_massiv





def search_week(lst: list) -> tuple:
    """находит лучшую и худщую неделю
    """
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





def search_month_sum(lst: list) -> list[tuple]:
    """ суммирует все дни месяцов
    """
    static_month = []
    lever = '01'
    summ = 0

    for i in range(0, len(lst), 1):

        if  lever == lst[i][0]:
            summ += int(lst[i][2])

            if len(lst) - 1 == i:
                static_month.append((lever, summ))
                return static_month

        else:
            static_month.append((lever, summ))
            summ = 0
            lever = lst[i][0]

    return static_month



def month_static(lst: list):
    """находит лучший и худший месяц
    """
    best_day = lst[0]
    worse_day = lst[0]
    best = lst[0][1]
    worse = lst[0][1]

    for i in range(1, len(lst), 1):
        if lst[i][1] > best:
            best = lst[i][1]
            best_day = lst[i]

        if lst[i][1] < worse:
            worse = lst[i][1]
            worse_day = lst[i]

        return (best_day, worse_day)









def main():
    mas = []

    file = open("data")

    for i in file:
        i = i.replace("2023", "").replace("-", " ").replace(",", " ").replace("\n", "")
        i = i.split(" ")
        del i[0]
        mas.append(i)


    magnitude = input(
        "Введите Д, если хотите узнать статустику в днях. Введите Н, если хотите узнать статистику в неделях."
        "Введите М, елси хотите узнать статистику в месяцах: ")



    if magnitude == "М":
        monthSUM = search_month_sum(mas)
        Mstatic = month_static(monthSUM)
        return (f"месяц: {Mstatic[0][0]}, результат: {Mstatic[0][1]} - лучший\n"
                f"месяц: {Mstatic[1][0]}, результат: {Mstatic[1][1]} - худший")

    if magnitude == "Н":
        month = input("введите месяц, в котором хотите узнать статистику: ")

        mas_month = create_monthMassiv(mas, month)
        week_static = search_week(mas_month)
        return (f"неделя: {week_static[0]}, результат: {week_static[1]} - лучшая\n"
                f"неделя: {week_static[2]}, результат: {week_static[3]} - худшая")


    if magnitude == "Д":
        month = input("введите месяц, в котором хотите узнать статистику: ")

        mas_month = create_monthMassiv(mas, month)
        day_static = search_day(mas_month)
        return (f"день: {day_static[0][1]}, результат: {day_static[0][2]} - лучший\n"
                f"день: {day_static[1][1]}, результат: {day_static[1][2]} - худший ")

    else:
        return f"некорректный запрос"
