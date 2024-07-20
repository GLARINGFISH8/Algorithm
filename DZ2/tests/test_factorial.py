# Аспекты
# Корректность счета
# Корректная работа с размерностью данных
# Корректная работа с разными типами данных

import pytest
from src.main1 import factorial

@pytest.mark.POL_factorial
@pytest.mark.parametrize("n, extend", [(5, 120),
                                       (1, 1),
                                       (3, 6)])

def test_factorialP(n, extend):
    assert factorial(n) == extend




@pytest.mark.BOUN_factorial
@pytest.mark.parametrize("n, extend", [(0, 1),
                                       (20, 2432902008176640000)])

def test_factorialB(n, extend):
    assert factorial(n) == extend




@pytest.mark.NEG_factorial
@pytest.mark.parametrize("n, extend", [(-20, pytest.raises(ValueError)),
                                       ("9", pytest.raises(TypeError)),
                                       (3.4, pytest.raises(TypeError)),
                                       (-1, pytest.raises(ValueError))])

def test_factorialN(n, extend):
    with extend:
        assert factorial(n) == extend