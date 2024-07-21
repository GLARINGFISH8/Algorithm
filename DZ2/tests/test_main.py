# Аспект
# Корректный счет
#
# ПодАспекты
# Корректный счет лучшего и худшего дня
# Корректный счет лучшей и худшей недели
# Корректный счет лучшего и худшего месяца

import pytest
from src import main5

def query_data():
    mas = []
    file = open("data1")

    for i in file:
        i = i.replace("2023", "").replace("-", " ").replace(",", " ").replace("\n", "")
        i = i.split(" ")
        del i[0]
        mas.append(i)

    return mas

@pytest.mark.DAY
@pytest.mark.parametrize("month, res", [("01", (['01', '05', '300'], ['01', '04', '100'])),
                                        ("02", ((['02', '28', '290'], ['02', '07', '170'])))])

def test_day(month, res):
    mas = query_data()
    mas_M = main5.create_monthMassiv(mas, month)
    assert main5.search_day(mas_M) == res



@pytest.mark.WEEK
@pytest.mark.parametrize("month, res", [("01", (3, 1570, 1, 1400)),
                                        ("02", (4, 1780, 1, 1460))])

def test_week(month, res):
    mas = query_data()
    mas_M = main5.create_monthMassiv(mas, month)
    assert main5.search_week(mas_M)



@pytest.mark.MONTH
@pytest.mark.parametrize("res", [(('01', 6630), ('02', 6290))])

def test_month(res):
    mas = query_data()
    sum_mas = main5.search_month_sum(mas)
    assert main5.month_static(sum_mas) == res





