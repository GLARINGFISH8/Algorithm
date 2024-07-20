# Аспекты
# Корректная работа с разными типами данных
# Корректность счета чисел фибоначи
# Корректная работ с размерностью данных
import pytest
from src.main2 import fibonacci

@pytest.mark.POL_fibonacci
@pytest.mark.parametrize("n, extend", [(10, [0, 1, 1, 2, 3, 5, 8, 13]),
                                       (1, [0, 1]),])

def test_fibonacciP(n, extend):
    assert fibonacci(n) == extend




@pytest.mark.BOUN_fibonacci
@pytest.mark.parametrize("n, extend", [(0, [0]),
                                       (100, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])])

def test_fibonacciB(n, extend):
    assert fibonacci(n) == extend



@pytest.mark.NEG_fibonacci
@pytest.mark.parametrize("n, extend", [(-1, pytest.raises(ValueError)),
                                       ("100", pytest.raises(TypeError))])

def test_fibonacciN(n, extend):
    with extend:
        assert fibonacci(n) == extend


        